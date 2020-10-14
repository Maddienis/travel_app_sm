import pandas as pd
import numpy as np
import food_city as fc
import survey_user
import sim_score
import attraction_city
import build_sim_matrix as build_sim
import survey_user
import city_combine

def startToEnd():
    
    food_city, food_city_name = fc.cityFoodMain()
    food_user = survey_user.createFoodUserDf()
    cosine_sim_food = sim_score.simScore(food_city, food_user)
    
    city_attraction, city_attraction_with_country = attraction_city.cityAttractionMain()
    user_attraction = survey_user.createAttractionUserDf()    
    cosine_sim_attraction = sim_score.simScore(city_attraction, user_attraction)
    
    full_sim_matrix = build_sim.createSimMatrixMain('survey_response', cosine_sim_food, cosine_sim_attraction, food_city_name)
    
    survey_clean = survey_user.transformSurveyMain('survey_response')
    
    full_city_data = city_combine.mergeAttractionFood(city_attraction_with_country, food_city)
    
    full_raw_matrix = build_sim.userCityCreate(survey_clean, full_city_data)
    
    finished = build_sim.finalMerge(full_raw_matrix, full_sim_matrix)
    
    return finished	

work = startToEnd()
print(work)