import pandas as pd 
import numpy as np 
import os




def column_selection(df):
	cols_to_keep = ['country', 'city', 'name', 'formatted_address',
	'price_level', 'rating', 'user_ratings_total', 'types',
	'geometry.location.lat', 'geometry.location.lng', 'place_id']

	df = df[cols_to_keep]

	df.rename(columns={'formatted_address': 'address',
		'geometry.location.lat': 'latitude', 'geometry.location.lng': 'longitude'})
	return df

	






