import pandas as pd 
import numpy as np 


def load_raw_df(places_df):
	raw_df = places_df

	return raw_df

def add_country_city(raw_df):
	code = raw_data['plus_code.compound_code'][0]
	split_code = code.split()
	country =  
	city = split_code[1]
	raw_df['country'], raw_df['city'] = [country, city]

def column_selection(df):
	cols_to_keep = ['country', 'city', 'name', 'formatted_address',
	'price_level', 'rating', 'user_ratings_total', 'types',
	'geometry.location.lat', 'geometry.location.lng', 'place_id']

	df = df[cols_to_keep]
	return df


	



