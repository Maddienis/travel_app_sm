import pandas as pd
import api_functions 
import utils
import db_connect as db

def city_query_selection(city_df, query_dict):
    for query in query_dict:
        for city in city_df.city:
            country = city_df.loc[city_df['city'] == city, 'country'].item()
            id = city_df.loc[city_df['city'] == city, 'id'].item()
            print('inside c q select', country, city, query_dict[query])
            pipeline(city, query_dict[query], country, id, query_dict)

    return 

def pipeline(city, query, country, id, query_dict):
    url = api_functions.build_url(city, query, country)
    data = api_functions.find_places_api(url)
    table_name = utils.find_table_name(query_dict, query)
    df = api_functions.create_df(data, city, country, id, table_name)
    db.write_db(table_name, df)
    
    return df


cities_df = db.get_city()

cities_one = cities_df.iloc[0:40, :].copy()
cities_two = cities_df.iloc[40:80, :].copy()
cities_three = cities_df.iloc[80:120, :].copy()
cities_four = cities_df.iloc[120:139, :].copy()

city_query_selection(cities_one, api_functions.query_dict)