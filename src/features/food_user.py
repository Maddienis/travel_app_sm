import pandas as pd
import numpy as np



# This will pull survey data from database and select only food columns
# Survey table is hardcoded
# Returns only food columns. index is user id

def createFoodUserDf():
    survey = get_df('survey_response')
    #survey = total.copy()
    food_user = survey[['food_one', 'food_two', 'food_three', 'food_four']]
    
    return food_user