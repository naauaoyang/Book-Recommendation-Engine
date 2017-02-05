
# coding: utf-8

import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('amazonRating').config("spark.some.config.option", "some-value").getOrCreate()

# read amazon review data
df = spark.read.json('/Users/naauao/Downloads/Books_5.json')
#df.show()
#df.count()

# see the distribution of ratings
df.groupBy("overall").count().orderBy("overall").show()


### Using reviewText to predict helpfulness
df = df.select(['reviewerID', 'asin', 'reviewText', 'overall'])
#df.show()

# use pandas to create helpfulness column
import pandas as pd
def parse(path):
    g = open(path, 'r')
    for l in g:
        yield eval(l)
def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = dict()
        helpful = d['helpful']
        if helpful[1] != 0:
            threshold = helpful[0] / helpful[1]
            if threshold >= 0.5:
                df[i]['helpful'] = 1
            else:
                df[i]['helpful'] = 0
            df[i]['reviewerID'] = d['reviewerID']
            df[i]['asin'] = d['asin']
            i += 1    
    return pd.DataFrame.from_dict(df, orient='index')
path = "/Users/naauao/Downloads/Books_5.json"
pandas_df = getDF(path)
#pandas_df.head()
#pandas_df.shape

# convert pandas dataframe to spark dataframe
df1 = spark.createDataFrame(pandas_df)
#df1.show()
#df1.count()

# use spark sql to join dataframes
df.createOrReplaceTempView("reviews")
df1.createOrReplaceTempView("reviews1")
df = spark.sql(
"""  
  SELECT reviews.reviewText as text, reviews.overall as rating, reviews1.helpful as label
  FROM reviews1 join reviews
  on reviews1.asin = reviews.asin
  and reviews1.reviewerID = reviews.reviewerID
  
"""
)
#df.show()
#df.count()

# see the distribution of helpfulness
df.groupBy("label").count().orderBy("label").show()

# make the helpfulness equally weighted because the original data is very imbalanced
df.createOrReplaceTempView("reviews")
df = spark.sql(
"""
  SELECT text, rating, label, rowNumber FROM (
    SELECT
       label, text, rating, row_number() OVER (PARTITION BY label ORDER BY rand()) AS rowNumber
    FROM reviews
  ) reviews
  WHERE rowNumber <= 800000
"""
)

# see the distribution of helpfulness
df.groupBy("label").count().orderBy("label").show()

# split train and test set
train = df.filter(df["rowNumber"] <= 600000).select("text", "rating", "label")
test = df.filter(df["rowNumber"] > 600000).select("text", "rating", "label")


# see the distribution of train set
train.groupBy("label").count().orderBy("label").show()

# see the distribution of test set
test.groupBy("label").count().orderBy("label").show()


### use Spark to do classification

from pyspark.ml import Pipeline
from pyspark.ml.classification import NaiveBayes, LogisticRegression
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.ml.feature import HashingTF, RegexTokenizer, StopWordsRemover, StringIndexer, VectorAssembler

# Configure an ML pipeline,
regexTokenizer = RegexTokenizer(inputCol="text", outputCol="words")
remover = StopWordsRemover(inputCol=regexTokenizer.getOutputCol(), outputCol="filtered")
hashingTF = HashingTF(inputCol=remover.getOutputCol(), outputCol="hashingfeatures")
stringIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel")
assembler = VectorAssembler(inputCols=['hashingfeatures', 'rating'], outputCol="features")
nb = NaiveBayes(labelCol=stringIndexer.getOutputCol())
#lr = LogisticRegression(maxIter=10, labelCol=stringIndexer.getOutputCol())
pipeline = Pipeline(stages=[regexTokenizer, remover, hashingTF, stringIndexer, assembler, nb])

# train the model
model = pipeline.fit(train)

# evaluate the result
result = model.transform(test)
predictionAndLabels = result.select("prediction", "indexedLabel")
predictionAndLabels = predictionAndLabels.rdd

#predictionAndLabels.take(10)

predictionAndLabels.persist()

metrics = MulticlassMetrics(predictionAndLabels)

# compute accuracy 
metrics.accuracy

# compute confusion matrix 
metrics.confusionMatrix()

# compute F1 score
metrics.fMeasure(label=1.0)


# plot confusion matrix
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np 
import itertools

cnf_matrix = metrics.confusionMatrix()
cnf_matrix = cnf_matrix.toArray()
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=['helpful', 'not helpful'], normalize=True,
                      title='Naive Bayes Normalized confusion matrix')
plt.show()


