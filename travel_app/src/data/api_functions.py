import pandas as pd
import numpy as np
import os

key = os.getenv('G_API_KEY')
query = 'restaurants+in+Bangkok'
base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?language=en&key={}'


def make_next_url(results, base_url):
  return base_url.format(key) + '&pagetoken={}'.format(results['next_page_token'])

def find_restaurants_az(url, data=[]):
  print(url)
  results = requests.get(url).json()
  time.sleep(5)
  data = data + results['results']
  print(results.keys())
  print(results['status'])
  if 'next_page_token' not in results.keys() and results['status']=='OK':
    print('no next')
    return data
  elif results['status']=='OK':
    print('next')
    new_url = make_next_url(results, base_url=base_url)
    return find_restaurants_az(new_url, data)
  else:
    return data

    