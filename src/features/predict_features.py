import pandas as pd
import numpy as np
import src.features.food_city as fc
import src.features.survey_user as survey_user
import src.features.sim_score as sim_score
import src.features.attraction_city as attraction_city
import src.features.build_sim_matrix as build_sim
import src.features.survey_user as survey_user
import src.features.city_combine as city_combine



def createPredictFeatures(user_data):
    
    food_city, food_city_name = fc.cityFoodMain()
    food_user = survey_user.createFoodUserDf()
    cosine_sim_food = sim_score.simScore(food_city, food_user)
    
    city_attraction, city_attraction_with_country = attraction_city.cityAttractionMain()
    #temp = attraction_city.cityAttractionMain()
    user_attraction = survey_user.createAttractionUserDf()    
    cosine_sim_attraction = sim_score.simScore(city_attraction, user_attraction)
    
    full_sim_matrix = build_sim.createSimMatrixMain(user_data, cosine_sim_food, cosine_sim_attraction, food_city_name)
    
    survey_clean = survey_user.transformSurveyMain(user_data)
    
    full_city_data = city_combine.mergeAttractionFood(city_attraction_with_country, food_city)
    
    full_raw_matrix = build_sim.userCityCreate(survey_clean, full_city_data)
    
    finished = build_sim.finalMerge(full_raw_matrix, full_sim_matrix)

    
    return finished	


def columnSelection(completed_matrix):
	slim_matrix = completed_matrix[['continent_city', 'food_sim', 'attraction_sim', 'sum', 'rank']]
	slim_matrix.sort_values('sum', ascending=False, inplace=True)

	return slim_matrix


def citySelection(slim_matrix, continent):
	print(continent)
	top_choice = slim_matrix.loc[slim_matrix['continent_city'] == continent].head(3)



	return top_choice


