import pandas as pd 
import numpy as np 
import streamlit as st 
import helper as hp
#from helper import load_data, describe_sample

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


def sort_attraction_data():
	data.sort_values('')
data = load_data()

st.dataframe(data)

st.write("What type of tourist attraction are you most interested in?")
attraction_type_selected = st.radio("Attraction Type", ['History', 
	'Place of Worship', 'Activity', 'Food', 'Nature'])

if attraction_type_selected == 'History':
	city = data.sort_values('history_count', ascending=False).reset_index(drop=True).city[0]
	st.write("You should go to ", city)
elif attraction_type_selected == 'Place of Worship':
	city = data.sort_values('place_of_worship_count', ascending=False).reset_index(drop=True).city[0]
	st.write("You should go to ", city)
elif attraction_type_selected == 'Activity':
	city = data.sort_values('activity_count', ascending=False).reset_index(drop=True).city[0]
	st.write("You should go to ", city)
elif attraction_type_selected == 'Food':
	city = data.sort_values('food_count', ascending=False).reset_index(drop=True).city[0]
	st.write("You should go to ", city)	
elif attraction_type_selected == 'Nature':
	city = data.sort_values('outdoor_count', ascending=False).reset_index(drop=True).city[0]
	st.write("You should go to ", city)
else:
	st.write("Will this work?")


def which_city_attraction():
	if attraction_type_selected == 'history':
		city = data.sort_values('history_count', ascending=False).index[0]
		st.write("You should go to ", city)

which_city_attraction()









