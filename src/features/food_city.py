import pandas as pd
import numpy as np
import seaborn as sns
import src.data.db_connect as db
import utils_feature as utils

#main call to create df for all food entries and city
def cityFoodMain():
    all_price = createFoodDf()
    all_price_ = cleaningNullsCity(all_price)
    food_city_level = toCityLevel(all_price_)
    food_city = addNanRowCity(food_city_level)
    final_food_city = selectColumns(food_city)
    
    return final_food_city, food_city


#1 hard coded with what tables to read from database
# Parameter input:
# Returns all of the food entires from database

def createFoodDf():
    one = db.get_df('restaurants_one')
    two = db.get_df('restaurants_two')
    three = db.get_df('restaurants_three')
    four = db.get_df('restaurants_four')
    top_rest = db.get_df('restaurants')
    
    all_price = pd.concat([one, two, three, four, top_rest], axis =0)
    return(all_price)


# This will fill price level null values that is the mean of the total restaurants for that city
# If that still does not fill it, it will fill with 2.
def cleaningNullsCity(restaurants_all):
    
    restaurants_all['id'] = pd.to_numeric(restaurants_all.id)
    restaurants_all['price_level'] = restaurants_all['price_level'].fillna(restaurants_all.groupby('city')['price_level'].transform('mean'))
    restaurants_all.fillna(2.0, inplace=True)
    #do I need this?
    restaurants_all['price_level'] = restaurants_all['price_level'].astype(int)
    
    
    return restaurants_all


# This will take the raw data for all restaurants and count the number for each city and price level.
 
def toCityLevel(df):

    city_df = df.groupby(['country', 'city', 'id', 'price_level'])['name'].count().to_frame()
    price_level = city_df.pivot_table(index=['country', 'city', 'id'], columns='price_level', values='name', aggfunc='first')
    price_level['avg_price'] = df.groupby(['country', 'city', 'id'])['price_level'].mean()
    price_level.drop(columns = ['avg_price'], inplace=True)
    price_level.fillna(0, inplace=True)
    
    
    return price_level


#4 called
def addNanRowCity(food_df):
    food_df.reset_index(inplace=True)
    nan_row = {'country' : None, 'city': 'Zx', 'id': 200, 1.0: 0, 2.0: 0, 3.0: 0, 4.0: 0}
    food_df = food_df.append(nan_row, ignore_index=True)
    
    global food_new 
    food_new = labelEncodeCity(food_df)
    food_new = food_new.drop(food_new[food_new.id == 200].index)
    
    return food_new


  
 # 5    
def labelEncodeCity(food_df):
    
    le = utils.buildLabelEncoder()
    food_df['label_id'] = le.transform(food_df.city)
    
    return food_df

# 7
def selectColumns(food_df):
    
    food_df = food_df.drop(food_df[food_df.id == 200].index)
    food_city = food_df[['label_id', 1.0, 2.0, 3.0, 4.0]].copy()
    food_city.sort_values('label_id', inplace=True)
    food_city.set_index('label_id', inplace=True)
    
    return food_city


