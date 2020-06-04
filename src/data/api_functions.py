import pandas as pd
import numpy as np
import os


key = os.getenv('G_API_KEY')
base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?language=en&key={}'


query_dict = {'attractions': "{}+points+of+interest",
  'restaurants': "best+restaurants+in+{}",
  'restaurants_price': 'best+restaurants+in+{}&minprice={}&maxprice={}'}

city_list = ['Portland', 'Krabi']



def build_query(city, query):
  if 'maxprice' in query:
    k = 1
    while k <= 4:
      url = base_url.format(key) + '&query={}'.format(query.format(city, k, k))
      k += 1 
      return url
            # DO I need a return for each k? 
    else:
        url = base_url.format(key) + '&query={}'.format(query.format(city))

  return url


def make_next_url(results, base_url):
  return base_url.format(key) + '&pagetoken={}'.format(results['next_page_token'])

def find_places_api(url, data=[]):
  print(url)
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
    new_url = make_next_url(results, base_url=base_url)
    return find_places_api(new_url, data)
  else:
    return data 

def create_df(json_data, city):
  #find_places_api()
  df = pd.json_normalize(json_data)
  city.replace('+', ' ')
  df['city'] = city
  df = column_selection(df)
  return df

    