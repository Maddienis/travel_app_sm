import pandas as pd
import numpy as n

# This pulls from survey table and selects only attraction colummns
def createAttractionUserDf():
    survey = get_df('survey_response')
    user_attraction = survey[['amusement_park', 'art_gallery', 'aquarium', 'library', 'movie_theater',
                              'museum', 'natural_feature', 'park', 'place_of_worship', 'shop', 'zoo']]
    return user_attraction