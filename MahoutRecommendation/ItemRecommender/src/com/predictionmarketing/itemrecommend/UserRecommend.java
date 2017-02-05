package com.predictionmarketing.itemrecommend;

import java.io.File;
import java.io.IOException;
import java.util.List;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.neighborhood.NearestNUserNeighborhood;
import org.apache.mahout.cf.taste.impl.recommender.GenericUserBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.EuclideanDistanceSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.LogLikelihoodSimilarity;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;

public class UserRecommend {

	public static void main(String[] args) {
		try {
			DataModel dm = new FileDataModel(new File("data/testresult_1.csv"));
			
			//UserSimilarity sim = new LogLikelihoodSimilarity(dm);
			UserSimilarity sim = new EuclideanDistanceSimilarity(dm);
			for(int i=101; i<8026324; i++){
			UserNeighborhood neighborhood = new NearestNUserNeighborhood(5, sim, dm);
			long[] neighbors = neighborhood.getUserNeighborhood(i);
			for (long user:neighbors){
				System.out.print(user+",");
			}
			System.out.printf("%n");
			}
			//GenericUserBasedRecommender recommender = 
					//new GenericUserBasedRecommender(dm,neighborhood,sim);
			
			//List<RecommendedItem> recommendations = recommender.recommend(17, 3);
			
			//for (RecommendedItem recommendation : recommendations){
				//System.out.println(recommendation);
			    //if(x>100) System.exit(1);
			//}

	}catch (IOException e) {
		System.out.println("There was an error.");
		e.printStackTrace();
	} catch (TasteException e) {
		System.out.println("There was a Taste Exception.");
		e.printStackTrace();
	}
	}

}
