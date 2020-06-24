import pandas as pd
import api_functions 
import utils
import db_connect as db

def city_query_selection(city_df, query_dict):
    for query in query_dict:
        for city in city_df.city:
            country = city_df.loc[city_df['city'] == city, 'country'].item()
            id = city_df.loc[city_df['city'] == city, 'id'].item()
            print('inside c q select', city, country, query_dict[query])
            table_name = utils.find_table_name(query_dict, query_dict[query])
            result = db.check_db(table_name, city)
            if result:
                print('inside if ')
                continue
            else:
                print('inside else')
                results_pipeline = pipeline(city, query_dict[query], country, id, query_dict, table_name)
                if results_pipeline is None:
                    continue
    return 

def pipeline(city, query, country, id, query_dict, table_name):
    url = api_functions.build_url(city, query, country)
    data = api_functions.find_places_api(url)
    if data == None:
        return None
    df = api_functions.create_df(data, city, country, id, table_name)
    db.write_db(table_name, df)
    
    return df


cities_df = db.get_city()

city_one = cities_df.iloc[0:40, :].copy()
city_two = cities_df.iloc[40:80, :].copy()
city_three = cities_df.iloc[80:100, :].copy()
city_four = cities_df.iloc[100:139, :].copy()
city_five = cities_df.iloc[120:139, :].copy()

city_query_selection(city_five, api_functions.QUERY_DICT)