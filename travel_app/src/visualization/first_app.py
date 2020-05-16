import pandas as pd 
import numpy as np 
import streamlit as st 

st.title("Travel App")

df = pd.read_csv('/Users/tristannisbet/Documents/SM/Dataframe/all_restaurants2.csv')

st.write("Here's the first table")
st.write(df)