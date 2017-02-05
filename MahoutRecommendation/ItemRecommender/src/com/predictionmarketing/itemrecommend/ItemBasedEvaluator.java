package com.predictionmarketing.itemrecommend;

import java.io.File;
import java.io.IOException;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.eval.RecommenderBuilder;
import org.apache.mahout.cf.taste.eval.RecommenderEvaluator;
import org.apache.mahout.cf.taste.impl.eval.AverageAbsoluteDifferenceRecommenderEvaluator;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.recommender.GenericItemBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.EuclideanDistanceSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.PearsonCorrelationSimilarity;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.recommender.Recommender;
import org.apache.mahout.cf.taste.similarity.ItemSimilarity;

public class ItemBasedEvaluator {

	public static void main(String[] args) throws Exception {
		DataModel model = new FileDataModel(new File("data/testresult_1.csv"));
		RecommenderEvaluator evaluator = new AverageAbsoluteDifferenceRecommenderEvaluator();
		RecommenderBuilder builder = new MyItemBasedRecommenderBuilder();
		double result = evaluator.evaluate(builder, null, model, 0.9, 1);
		System.out.println(result);

	}

}

class MyItemBasedRecommenderBuilder implements RecommenderBuilder{
	public Recommender buildRecommender(DataModel dataModel) 
			throws TasteException{
		ItemSimilarity similarity = new PearsonCorrelationSimilarity(dataModel);
		return new GenericItemBasedRecommender(dataModel,similarity);
	}
} 

