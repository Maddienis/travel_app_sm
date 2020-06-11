import pandas as pd
import numpy as np
import os
import json, requests
import time

key = os.getenv('G_API_KEY')
BASE_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?language=en&key={}'
QUERY_DICT = {'attractions': "{}+points+of+interest",
              'restaurants': "best+restaurants+in+{}",
             'restaurants_one': 'best+restaurants+in+{}&minprice=1&maxprice=1',
             'restaurants_two': 'best+restaurants+in+{}&minprice=2&maxprice=2',
             'restaurants_three': 'best+restaurants+in+{}&minprice=3&maxprice=3',
             'restaurants_four': 'best+restaurants+in+{}&minprice=4&maxprice=4'}


def build_url(city, query, country):
    cc = [city, country]
    cc = '+'.join(cc)
    url = BASE_URL.format(key) + '&query={}'.format(query.format(cc))
    return url


def make_next_page_url(results, base_url):
    return BASE_URL.format(key) + '&pagetoken={}'.format(results['next_page_token'])


def find_places_api(url, data=[]):
    results = requests.get(url).json()
    time.sleep(7)
    data = data + results['results']
    print(results.keys())
    print(results['status'])
    status = results['status']
    if status == 'ZERO_RESULTS':
        return None
    elif 'next_page_token' not in results.keys() and results['status']=='OK':
        print('no next')
        return data
    elif results['status']=='OK':
        print('next')
        new_url = make_next_page_url(results, base_url=BASE_URL)
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
    cols_to_keep = ['country', 'city', 'name', 'formatted_address', 'price_level',
                'rating', 'user_ratings_total', 'types', 'place_id', 'id']
    for col in cols_to_keep:
        if col not in df:
            df[col] = None

    df = df[cols_to_keep].copy()
    df.rename(columns={'formatted_address': 'address',
                       'geometry.location.lat': 'latitude',
                       'geometry.location.lng': 'longitude'}, inplace=True)
    df['types'] = df.types.astype(str)
    
    return df


 