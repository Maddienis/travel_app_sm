import pandas as pd
import numpy as np
import os


key = os.getenv('G_API_KEY')
base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?language=en&key={}'


query_list = ["{}+points+of+interest", "best+restaurants+in+{}"]
city_list = ['Portland', 'Krabi']



def build_query(city_list, query_list):
  for city in city_list:
      for query in query_list:
          url = base_url.format(key) + '&query={}'.format(query.format(city))
          data = find_places_api(url, city)

  return data


def make_next_url(results, base_url):
  return base_url.format(key) + '&pagetoken={}'.format(results['next_page_token'])

def find_places_api(url, city, data=[]):
  print(url)
  results = requests.get(url).json()
  time.sleep(5)
  data = data + results['results']
  print(results.keys())
  print(results['status'])
  if 'next_page_token' not in results.keys() and results['status']=='OK':
    print('no next')
    return create_df(data, city)
  elif results['status']=='OK':
    print('next')
    new_url = make_next_url(results, base_url=base_url)
    return find_places_api(new_url, city, data)
  else:
    return create_df(data, city)

def create_df(json_data, city):
  df = pd.json_normalize(json_data)
  df['city'] = city
  # Add id, and country also.
  # ADD TO TABLE??
  return df

    