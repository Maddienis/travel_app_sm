import pandas as pd
import numpy as np
import ast
import src.features.utils_feature as utils
import src.data.db_connect as db

PLACE_OF_WORSHIP = ['place_of_worship', 'hindu_temple', 'church', 'mosque', 'synagogue']
SHOPPING = ['store', 'shopping_mall', 'clothing_store', 'electronics_store', 'grocery_or_supermarket', 'department_store']

ATTRACTIONS_TO_KEEP = ['amusement_park', 'museum', 'park', 'art_gallery', 'aquarium',
                      'zoo', 'library', 'movie_theater', 'natural_feature'] + PLACE_OF_WORSHIP + SHOPPING


# Pulls all attraction data from database. Will groupby each attraction type that I want to keep and count.
# Returns: Each city with a count for the specified attractions

# Hard coded attractions table
def cityAttractionMain():
    attractions_df = db.get_df('attractions')
    attractions_split = splitTypes(attractions_df)
    dummy = dummies(attractions_split)
    by_city, all_attractions = attractionCount(dummy, attractions_split)
    city_group = combineAttractionTypes(by_city)
    city_attraction = labelEncodeAttraction(city_group)
    clean_city_attraction, city_attraction = cleanCityAttraction(city_attraction)
    
    return clean_city_attraction, city_attraction

def splitTypes(df):
    df['split_types'] = [ast.literal_eval(x) for x in df.types]
    df['split_types_str'] = [','.join(x) for x in df.split_types]
    
    return df

def dummies(df):
    dummies = df.split_types_str.str.get_dummies(sep=',')

    return dummies


def attractionCount(dummies_df, all_attractions_df):
    
    all_attractions_df = pd.concat([all_attractions_df, dummies_df], axis=1)
    type_col_names = []
    type_col_names = ATTRACTIONS_TO_KEEP.copy()
    type_col_names.extend(['country', 'city', 'id'])
    attraction_count = all_attractions_df[type_col_names].groupby(['country', 'city', 'id']).sum()

    return attraction_count, all_attractions_df

def combineAttractionTypes(city_group):
    print("IN COMBINE ATTRACTION type")
    city_group['place_of_worship2'] = city_group['place_of_worship'] + city_group['hindu_temple'] + city_group['church'] + city_group['mosque'] + city_group['synagogue']
    city_group['store2'] = city_group['store'] + city_group['shopping_mall'] + city_group['clothing_store'] + city_group['electronics_store'] + city_group['grocery_or_supermarket'] + city_group['department_store']
    
    city_group.rename(columns={"place_of_worship2" : 'place_of_worship', 'store2': 'shop', "place_of_worship" : 'place_of_worship5',}, inplace=True)
    
    city_clean = city_group[['amusement_park', 'art_gallery', 'aquarium', 'library', 'movie_theater',
                              'museum', 'natural_feature', 'park', 'place_of_worship', 'shop', 'zoo']].copy()
    
    return city_clean


def labelEncodeAttraction(city_attraction):
    le = utils.buildLabelEncoder()
    city_attraction.reset_index(inplace=True)
    city_attraction['label_id'] = le.transform(city_attraction.city)
    
    return city_attraction


def cleanCityAttraction(city_attraction):
    city_attraction.sort_values('label_id', inplace=True)
    city_attraction.set_index('label_id', inplace=True)
    city_attraction.drop(columns=['id'], inplace=True)
    city_attraction_clean = city_attraction.drop(columns=['city', 'country'])
    
    return city_attraction_clean, city_attraction
    