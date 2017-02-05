package com.predictionmarketing.itemrecommend;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.List;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.eval.RecommenderIRStatsEvaluator;
import org.apache.mahout.cf.taste.impl.common.LongPrimitiveIterator;
import org.apache.mahout.cf.taste.impl.eval.GenericRecommenderIRStatsEvaluator;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.recommender.GenericItemBasedRecommender;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.similarity.ItemSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.EuclideanDistanceSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.LogLikelihoodSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.PearsonCorrelationSimilarity;

public class ItemBasedRecommender_Sim {

	public static void main(String[] args) {
		try {
			DataModel dm = new FileDataModel(new File("data/testresult_1.csv"));
			//ItemSimilarity sim = new LogLikelihoodSimilarity(dm);
			//ItemSimilarity sim = new PearsonCorrelationSimilarity(dm);
			ItemSimilarity sim = new EuclideanDistanceSimilarity(dm);
			
			GenericItemBasedRecommender recommender = 
					new GenericItemBasedRecommender(dm,sim);
			
			
			
			//BufferedWriter bw = new BufferedWriter(new FileWriter("/Users/huashuli/Downloads/recommender_result.csv"));
			//FileOutputStream fos = new FileOutputStream("/Users/huashuli/Downloads/recommender_result.csv");
			//ObjectOutputStream oos = new ObjectOutputStream(fos); 
			
			//for(int i=0; i<8026324; i++){
				//oos.writeObject(i);
				//bw.write(i);
				//bw.newLine();
				//System.out.println(i);
            //List<RecommendedItem> recommendations = recommender.recommend(i, 3);
			
			//for (RecommendedItem recommendation : recommendations){
				//bw.write(recommendation);
				//bw.newLine();
				//oos.writeObject(recommendation.getItemID() + "," + recommendation.getValue()+"\n");
				//System.out.println(recommendation.getItemID()+","+recommendation.getValue());
				//}
			//}
			//bw.close();
			//oos.close(); 
			//int x=1;
			//for(LongPrimitiveIterator items = dm.getItemIDs(); items.hasNext();){
				//long itemId = items.nextLong();
				//List<RecommendedItem>recommendations = recommender.mostSimilarItems(itemId, 2);
			    //for(RecommendedItem recommendation : recommendations){
			    	//System.out.println(itemId + "," + recommendation.getItemID() + "," + recommendation.getValue());
			    //}
			    //x++;
			    //if(x>100) System.exit(1);
			//}
			
		} catch (IOException e) {
			System.out.println("There was an error.");
			e.printStackTrace();
		} catch (TasteException e) {
			System.out.println("There was a Taste Exception.");
			e.printStackTrace();
		}
		

	}

}

