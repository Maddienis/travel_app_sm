import pandas as pd
import numpy as np
import os
import json, requests
import time

key = os.getenv('G_API_KEY')
base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?language=en&key={}'
query_dict = {'attractions': "{}+points+of+interest",
              'restaurants': "best+restaurants+in+{}",
             'restaurants_one': 'best+restaurants+in+{}&minprice=1&maxprice=1',
             'restaurants_two': 'best+restaurants+in+{}&minprice=2&maxprice=2',
             'restaurants_three': 'best+restaurants+in+{}&minprice=3&maxprice=3',
             'restaurants_four': 'best+restaurants+in+{}&minprice=4&maxprice=4'}



def build_url(city, query, country):
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?language=en&key={}'
    cc = [city, country]
    cc = '+'.join(cc)
    url = base_url.format(key) + '&query={}'.format(query.format(cc))
    return url


def make_next_page_url(results, base_url):
    return base_url.format(key) + '&pagetoken={}'.format(results['next_page_token'])


def find_places_api(url, data=[]):
    results = requests.get(url).json()
    time.sleep(3)
    data = data + results['results']
    print(results.keys())
    print(results['status'])
    if 'next_page_token' not in results.keys() and results['status']=='OK':
        print('no next')
        return data
    elif results['status']=='OK':
        print('next')
        new_url = make_next_page_url(results, base_url=base_url)
        return find_places_api(new_url, data)
    else:
        return data 


def create_df(json_data, city, country, id, table_name):
    df = pd.json_normalize(json_data)
    df['city'] = city.replace('+', ' ')
    df['country'] = country.replace('+', ' ')
    df['id'] = id
    df = column_selection(df, table_name)
    return df


def column_selection(df, table_name):
    if table_name == 'attractions':
        cols_to_keep = ['country', 'city', 'name', 'formatted_address',
                        'rating', 'user_ratings_total', 'types',
                        'geometry.location.lat', 'geometry.location.lng', 'place_id', 'id']
    else:
        cols_to_keep = ['country', 'city', 'name', 'formatted_address', 'price_level',
                        'rating', 'user_ratings_total', 'types',
                        'geometry.location.lat', 'geometry.location.lng', 'place_id', 'id']
    
    df = df[cols_to_keep].copy()
    df.rename(columns={'formatted_address': 'address',
                       'geometry.location.lat': 'latitude',
                       'geometry.location.lng': 'longitude'}, inplace=True)
    df['types'] = df.types.astype(str)
    
    return df


 