import pandas as pd 
import numpy as np 
import streamlit as st 
import helper as hp

st.title("Travel App")

df = pd.read_csv('/Users/tristannisbet/Documents/SM/Dataframe/all_restaurants2.csv')

st.write("Here's the first table")
st.write(df)



option = st.sidebar.selectbox(
    'Which number do you like best?',
     [1,2,3,4,5])




values = st.slider(
	'What price level are you most likely to eat at?',
	0, 4, (1, 2))
st.write('Values:', values)




@st.cache
def load_data():
    return pd.read_csv("/Users/tristannisbet/Documents/SM/Dataframe/attractions_count.csv")


data = load_data()

st.dataframe(data)

st.write("What type of tourist attraction are you most interested in?")
attraction_type_selected = st.radio("Attraction Type", ['History', 
	'Place of Worship', 'Activity', 'Food', 'Nature'])

def which_city_attraction(radio_choice):
	type_to_df_dict = {'History': 'history_count', 'Place of Worship': 'place_of_worship_count',
	'Activity': 'activity_count', 'Food': 'food_count', 'Nature': 'outdoor_count'}
	if radio_choice in type_to_df_dict:
		city = data.sort_values(type_to_df_dict[radio_choice], ascending=False).reset_index(drop=True).city[0]
		return city

def city_output(city):
	st.write('You should visit ', city)

# Funciton call
city_output(which_city_attraction(attraction_type_selected))








