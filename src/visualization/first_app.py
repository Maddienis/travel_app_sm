import pandas as pd 
import numpy as np 
import streamlit as st 
import helper as hp
import pydeck as pdk
import folium


@st.cache
def load_data_attraction(file_path):
    attraction_data_new = pd.read_csv(file_path, index_col=[0])
    attraction_data_new.rename(columns={'geometry.location.lat': 'latitude', 'geometry.location.lng': 'longitude'}, inplace=True)
    attraction_data_new.set_index(['city', 'country'], inplace=True)
    return attraction_data_new

def load_data(file_path):
	return pd.read_csv(file_path, index_col=[0])


st.title("What city should you travel to?")

st.subheader('User Info')

home_country = st.selectbox('What country are you from?', ('USA', 'AUS', 'Thailand'))
st.text("")
travel_area = st.selectbox('What region do you want to travel to?', ('North America', 
	'South America', 'Europe', 'Asia', 'Oceananic', 'Africa'))

st.text("")
st.text("")
st.subheader("Food")
values = st.slider(
	'What price level are you most likely to eat at?',
	0, 4, (1, 2))
st.write('Values:', values)

st.write("")
st.subheader("Tourist Attractions")

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
	lat = df.latitude[0]
	lon = df.longitude[0]

	st.write("You should go to ", city)
	st.map(df, zoom=10)


data = load_data("/Users/tristannisbet/Documents/SM/Dataframe/attractions_count.csv")

attraction_data = load_data_attraction("/Users/tristannisbet/Documents/SM/Dataframe/all_attractions.csv")


# Funciton call
display_map(which_city_attraction(attraction_type_selected))


world_map = folium.Map(location=[38.8934, -76.9470], zoom_start=8)
st.markdown(world_map._repr_html_(), unsafe_allow_html=True)


if __file__.name = 



