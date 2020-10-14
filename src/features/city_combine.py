import pandas as pd
import numpy as np
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2



# This will merge attraction and food on the city level all numeric passes it to add the continent of each city
def mergeAttractionFood(attraction_df, food_df):
    
    city = pd.merge(left = attraction_df, right = food_df, left_index = True, right_index=True)
    
    city_cont = addContinent(city)
    
    return city_cont



def addContinent(city_df):
    continents = {
    'NA': 'North America',
    'SA': 'South America', 
    'AS': 'Asia',
    'OC': 'Australia',
    'AF': 'Africa',
    'EU': 'Europe'}
    
    city_df['continent'] = [continents[country_alpha2_to_continent_code(country_name_to_country_alpha2(country))] for country in city_df['country']]
    city_df.set_index(['city', 'country'], append=True, inplace=True)
    
    #city_cont_dummy = dummyContinent(city_df)
    
    return city_df


def dummyContinent(city_df):
    
    city_dummy = pd.get_dummies(city_df)
    
    return city_dummy