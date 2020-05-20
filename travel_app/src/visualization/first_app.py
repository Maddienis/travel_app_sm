import pandas as pd 
import numpy as np 
import streamlit as st 
import helper as hp

st.title("Travel App")

df2 = pd.read_csv('/Users/tristannisbet/Documents/SM/Dataframe/all_restaurants2.csv')

st.write("Here's the first table")
st.write(df2)



option = st.sidebar.selectbox(
    'Which number do you like best?',
     [1,2,3,4,5])




values = st.slider(
	'What price level are you most likely to eat at?',
	0, 4, (1, 2))
st.write('Values:', values)




@st.cache
def load_data_attraction(file_path):
    attraction_data_new = pd.read_csv(file_path, index_col=[0])
    attraction_data_new.rename(columns={'geometry.location.lat': 'latitude', 'geometry.location.lng': 'longitude'}, inplace=True)
    attraction_data_new.set_index(['city', 'country'], inplace=True)
    return attraction_data_new

def load_data(file_path):
	return pd.read_csv(file_path, index_col=[0])




data = load_data("/Users/tristannisbet/Documents/SM/Dataframe/attractions_count.csv")

attraction_data = load_data_attraction("/Users/tristannisbet/Documents/SM/Dataframe/all_attractions.csv")



st.write("What type of tourist attraction are you most interested in?")
attraction_type_selected = st.radio("Attraction Type", ['History', 
	'Place of Worship', 'Activity', 'Food', 'Nature'])

def which_city_attraction(radio_choice):
	type_to_df_dict = {'History': 'history_count', 'Place of Worship': 'place_of_worship_count',
	'Activity': 'activity_count', 'Food': 'food_count', 'Nature': 'outdoor_count'}
	if radio_choice in type_to_df_dict:
		city = data.sort_values(type_to_df_dict[radio_choice], ascending=False).reset_index(drop=True).city[0]
		return city


def display_map(city):
	df = attraction_data.loc[city].copy()
	st.write("You should go to ", city)
	st.map(df, zoom=0)


# Funciton call
display_map(which_city_attraction(attraction_type_selected))




# st.write("This is the attraction data for each city")
# st.write(attraction_data)

# st.title("Map")

# bk = attraction_data.set_index(['country', 'city']).loc['Thailand']

# bk.rename(columns={'geometry.location.lat': 'latitude', 'geometry.location.lng': 'longitude'}, inplace=True)

# st.map(bk)






