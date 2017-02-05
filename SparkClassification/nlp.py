def get_words(url):
    import requests
    words = requests.get(url).content.decode('latin-1')
    word_list = words.split('\n')
    index = 0
    while index < len(word_list):
        word = word_list[index]
        if ';' in word or not word:
            word_list.pop(index)
        else:
            index+=1
    return word_list

#Get lists of positive and negative words
p_url = 'http://ptrckprry.com/course/ssd/data/positive-words.txt'
n_url = 'http://ptrckprry.com/course/ssd/data/negative-words.txt'
positive_words = get_words(p_url)
negative_words = get_words(n_url)
def remove_punctuation(word):
    if word and ((word[-1] >= 'a' and word[-1]<='z') or (word[-1] >= 'A' and word[-1]<='Z')):
        return word
    elif word:
        return word[:-1]
    else:
        return word

import json
lengthw=[]
pos_neg=[]
with open('/Users/huashuli/Downloads/reviews_Books_5.json') as f:
    for line in f:
        words = json.loads(line)['reviewText'].split()
        cpos=0
        cneg=0
        for word in words:
            word = remove_punctuation(word)
            if word in positive_words:
                cpos += 1
            if word in negative_words:
                cneg += 1
        total_words = len(words)
        if cneg==0:
            pos_neg_ratio=0
        else:
            pos_neg_ratio = cpos/cneg
        lengthw.append(total_words)
        pos_neg.append(pos_neg_ratio)

import pandas as pd
lengthw_p=pd.DataFrame({'lengthw':lengthw})
lengthw_p.to_csv("/Users/huashuli/Downloads/lengthw_v.csv", index=False)

pos_neg_p=pd.DataFrame({'pos_neg':pos_neg})
pos_neg_p.to_csv("/Users/huashuli/Downloads/pos_neg_v.csv",index=False)

import json
import pandas as pd
data_helpful = []
data_review = []
data_rating = []
with open('/Users/huashuli/Downloads/reviews_Books_5.json') as f:
    for line in f:
        data_helpful.append(json.loads(line)['helpful'])
        data_review.append(json.loads(line)['reviewText'])
        data_rating.append(json.loads(line)['overall'])
combined_data = pd.DataFrame({'helpful':data_helpful,'review':data_review,'rating':data_rating})

length = []
for index,row in combined_data.iterrows():
    length.append(len(row['review']))

length_p=pd.DataFrame({'length':length})
length_p.to_csv("/Users/huashuli/Downloads/length_v.csv", index=False)
length=pd.read_csv("/Users/huashuli/Downloads/length_v.csv")
helpful=pd.read_csv("/Users/huashuli/Downloads/jsonHelpfulOnlyFraction.csv")
length=length[0:705205]
helpful=helpful[0:705205]
lengthw_p['avg_length']=np.where(lengthw_p['lengthw']==0,0,length['length']/lengthw_p['lengthw'])
def partition(x):
    if x < 0.5:
        return 'unhelpful'
    return 'helpful'
tmp=helpful
tmp['Helpful'] = tmp['Helpful'].map(partition)
tmp.to_csv("/Users/huashuli/Downloads/boolean_v.csv")
data_review=[]
i=0
with open('/Users/huashuli/Downloads/reviews_Books_5.json') as f:
        for line in f:
            if i<705205:
                data_review.append(json.loads(line)['reviewText'])
                i+=1
review_p=pd.DataFrame({'review':data_review})
frame = pd.concat([tmp,review_p],axis=1)

#wordcloud
from wordcloud import WordCloud
import nltk
import string
import matplotlib.pyplot as plt
helpful_words = ''
unhelpful_words = ''
intab = string.punctuation
outtab = "                                "
trantab = str.maketrans(intab, outtab)
pos = frame.loc[frame['Helpful'] == 'helpful']
pos = pos[0:10000]

neg = frame.loc[frame['Helpful'] == 'unhelpful']
neg = neg[0:10000]
from nltk.corpus import stopwords
for val in pos["review"]:
    text = val.lower()
    text = text.translate(trantab)
    #find the words and punctuation in a string
    tokens = nltk.word_tokenize(text)
    #remove punctuations
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    for words in tokens:
        helpful_words = helpful_words + words + ' '
for val in neg["review"]:
    text = val.lower()
    text = text.translate(trantab)
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    for words in tokens:
        unhelpful_words = unhelpful_words + words + ' '
DELETE_WORDS = ['character','story','novel','one','two','time','first','reader','author','read','book','reading','people','written']
def remove_words(text_string,DELETE_WORDS=DELETE_WORDS):
    for word in DELETE_WORDS:
        text_string = text_string.replace(word,' ')
    return text_string
helpful_words_1=remove_words(helpful_words)
helpful_words_1=remove_short_words(helpful_words_1)

%matplotlib inline
plt.ion()
print ("Helpful Review Word-Cloud")
wordcloud = WordCloud(max_font_size=40,background_color='white').generate(helpful_words_1)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

%matplotlib inline
plt.ion()
print ("Unhelpful Review Word-Cloud")
wordcloud = WordCloud(max_font_size=40,background_color='white').generate(unhelpful_words_1)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

