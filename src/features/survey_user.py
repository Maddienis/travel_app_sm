import pandas as pd
import numpy as np
import src.features.utils_feature as utils 
import src.data.db_connect as db

# This pulls from survey table and selects only attraction colummns
# Returns only attraction data to be normalized and sim score
def createAttractionUserDf(data='survey_response'):
    if type(data) == str:
        survey = db.get_df('survey_response')
        user_attraction = survey[['amusement_park', 'art_gallery', 'aquarium', 'library', 'movie_theater',
                              'museum', 'natural_feature', 'park', 'place_of_worship', 'shop', 'zoo']]
    else:
        print(data)
        print("INSIDE ELSE")
        user_attraction = data[['amusement_park', 'art_gallery', 'aquarium', 'library', 'movie_theater',
                              'museum', 'natural_feature', 'park', 'place_of_worship', 'shop', 'zoo']]

    return user_attraction



# This will pull survey data from database and select only food columns
# Survey table is hardcoded
# Returns only food columns. index is user id to be normalized and sim score

def createFoodUserDf(data='survey_response'):
    if type(data) == str:
        survey = db.get_df('survey_response')
        food_user = survey[['food_one', 'food_two', 'food_three', 'food_four']]

    else:
        food_user = data[['food_one', 'food_two', 'food_three', 'food_four']]
            
    return food_user


def transformSurveyMain(table_name):
    survey_nat = nationalityToNumeric(table_name)
    survey_city = encodeTopCity(survey_nat)
    survey_dummy = userDemographicDummy(survey_city)

    return survey_dummy

# This will transform the survey data into all numeric

def nationalityToNumeric(data):
    if type(data) == str:
        survey = db.get_df(data)
        survey.drop(columns=[''], inplace=True)
        survey = survey.replace({'': 'Zx'})


    else:
        survey = data
        survey = survey.replace({None: 'Zx'})

    nationality_dict = {'Australia': 1, 'Canada': 2, 'China': 3, 'Finland': 4, 'Honduras': 5,
              'India': 6, 'Israel': 7, 'Japan': 8, 'Mexico': 9, 'Pakistan': 10, 'Philippines': 11, 'United States': 12}

    survey.nationality = survey.nationality.map(nationality_dict)
    
    return survey



def encodeTopCity(user_response):
    
    le = utils.buildLabelEncoder()
    user_response['one'] = le.transform(user_response['favorite_city_one'])
    user_response['two'] = le.transform(user_response['favorite_city_two'])
    user_response['three'] = le.transform(user_response['favorite_city_three'])
    user_response['four'] = le.transform(user_response['favorite_city_four'])
    user_response['five'] = le.transform(user_response['favorite_city_five'])

    user_response = user_response.apply(pd.to_numeric, errors='ignore')

    
    return user_response


def userDemographicDummy(user_response):
    
    ready = user_response.drop(columns=['favorite_city_one', 'favorite_city_two', 'favorite_city_three',
                                          'favorite_city_four', 'favorite_city_five'])
    dummy = pd.get_dummies(ready)
    
    return dummy

