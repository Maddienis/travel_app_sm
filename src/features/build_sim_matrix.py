import pandas as pd
import numpy as np
import src.data.db_connect as db

# This will create the full dataset of all sim scores, sum, and the rank. UserxCity
# Survey response data


# Main function call
def createSimMatrixMain(table_name, cosine_sim_food, cosine_sim_attraction, food_df_city_name):
    
    top_city_melt = addTopCity(table_name)
    top_city_no_na = dropNullRankCity(top_city_melt)
    
    sim_df = createUserCitySimMatrix(cosine_sim_food, food_df_city_name)
    matrix_full = addAttractionSimMatrix(sim_df, cosine_sim_attraction)
    final_matrix = addSumColumn(matrix_full)
    clean = cleanMatrix(final_matrix)

    sim_matrix_ready = mergeRanktoMatrix(clean, top_city_no_na)
    
    return sim_matrix_ready


# This melts the cosine sim matrix that is userXcity to create my dataset where every userxcity combo is there
# Start with the cosine_food
# Could maybe pull out first couple lines and create own function...


def createUserCitySimMatrix(cosine_sim_food, food_df_city_name):
    cosine_food = cosine_sim_food.reset_index()
    cos_melt = cosine_food.melt(id_vars=['index'], value_name="food_sim", var_name = "city_id")
    cos_melt.rename(columns={'index': 'user'}, inplace=True)
    cos_melt['city_id'] = cos_melt['city_id'].astype(int)
    
    city_dict = dict(zip(food_df_city_name['label_id'], food_df_city_name['city']))
    
    cos_melt['city'] = cos_melt['city_id'].map(city_dict)
    

    return cos_melt


# melts attraction cosine matrix and then merges with the melted city matrix
def addAttractionSimMatrix(user_city_matrix, cosine_sim_attraction):
    cosine_attraction = cosine_sim_attraction.reset_index()
    cos_melt = cosine_attraction.melt(id_vars=['index'], value_name="attraction_sim", var_name = "city_id")
    cos_melt['city_id'] = cos_melt['city_id'].astype(int)
    
    sim_matrix = pd.merge(right=user_city_matrix, left=cos_melt, right_on=['user', 'city_id'], left_on=['index', 'city_id'])
    
    
    return sim_matrix


# Sums up food sime and attration sim and create a new column
def addSumColumn(sim_score_matrix):
        
    sim_score_matrix['sum'] = sim_score_matrix['food_sim'] + sim_score_matrix['attraction_sim']
    
    return sim_score_matrix


def cleanMatrix(matrix):
    
    matrix.drop(columns=['index'], inplace=True)
    clean = matrix[['user', 'city_id', 'city', 'food_sim', 'attraction_sim', 'sum']]
    clean.set_index(['user', 'city'], inplace=True)
    
    return clean

#Might move these functions down
# This is add a rank of 1 to the users top rated cities

# Melts the dataframe into user and top favorite city
def addTopCity(table_name):
    survey = db.get_df(table_name)

    top_city = survey[['favorite_city_one', 'favorite_city_two', 'favorite_city_three', 'favorite_city_four', 'favorite_city_five']].copy()
    
    top_city.reset_index(inplace=True)
    top_city.rename(columns={'index': 'user'}, inplace=True)
    top_city = top_city.replace({'': np.nan})
    top_city_melt = top_city.melt(id_vars=['user'])
    
    top_city_melt['rank'] = top_city_melt.apply(rank_from_col,axis=1)


    return top_city_melt


# Adds a column of 1s if the userxcity row is a favorite city
def rank_from_col(x):
    if x.variable=='favorite_city_one':
       return 1
    elif x.variable=='favorite_city_two':
       return 1
    elif x.variable=='favorite_city_three':
       return 1
    elif x.variable=='favorite_city_four':
       return 1
    elif x.variable=='favorite_city_five':
       return 1
    elif x.value == 'None':
        return 0 


#Drops city ranks with Null values as city
#Sets index
def dropNullRankCity(top_city_melt):
    top_city_no_na = top_city_melt.dropna().copy()
    top_city_no_na.rename(columns={'value':'city'}, inplace=True)
    top_city_no_na.set_index(['user', 'city'], inplace=True)
    
    return top_city_no_na

# Might move this function up


# This is the final merge to add the rankings of each user with the sim scores
def mergeRanktoMatrix(sim_df, rank_df):
    
    sim_matrix = pd.merge(left=sim_df, right=rank_df[['rank']], left_index=True, right_index=True, how='left')
    sim_matrix.fillna(0, inplace=True)
    sim_matrix.sort_values('user', inplace=True)
    sim_matrix.set_index('city_id', append=True, inplace=True)

    return sim_matrix


# All of this below is a separate main call

def userCityCreate(survey_df_clean, city_df_all):
    
    
    reindex_survey = survey_df_clean.reset_index()
    reindex_city = city_df_all.reset_index()
    reindex_city = reindex_city.add_suffix('_city')
    reindex_survey = reindex_survey.add_suffix('_user')
    reindex_city['key'] = 1
    reindex_survey['key'] = 1
    
    full = pd.merge(reindex_city , reindex_survey, on='key').drop('key',axis=1)
    
    raw_inputs_matrix = cleanUserCityMatrix(full)

    return raw_inputs_matrix

def cleanUserCityMatrix(matrix):
    
    matrix.rename(columns={'label_id_city': 'city_id', 'city_city': 'city', 'index_user': 'user'}, inplace=True)
    matrix.drop(columns=['country_city'], inplace=True)
    matrix.set_index(['user', 'city', 'city_id'], inplace=True)
    matrix.sort_index(level=0, inplace=True)

    return matrix
    

def finalMerge(raw_df, sim_score_df):
    full_matrix = pd.merge(left= raw_df, right= sim_score_df, right_index=True, left_index=True)
    full_matrix.sort_index(level=0, inplace=True)

    return full_matrix





