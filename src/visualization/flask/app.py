import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
import src.features.predict_features as predict_features
import src.data.db_connect as db

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# Can add /home or leave it. 
@app.route('/', methods=['GET', 'POST'])
def index():
	
	return render_template('starter_template_new.html')



#if request.method == "POST":
		#Can delete this
		#global req
		#req = request.form

		#top_city = request.form.getlist('topcity')

		#print(top_city)
		#d = request.form.to_dict()
		#df = pd.DataFrame([d])
#return redirect(url_for('recommend', data=df)

#@app.route('/', methods=["GET", "POST"])
@app.route('/results', methods=['POST'])
def results():
	if request.method == "POST":
		d = request.form.to_dict()
		df = pd.DataFrame([d])
		top_city = request.form.getlist('topcity')
		global CONTINENT_CHOICE 
		CONTINENT_CHOICE = request.form.get('continent')
		dict_keys = []
		for city_num in range(len(top_city)):
			dict_keys.append(city_num)

		city_dict = dict(zip(dict_keys, top_city))
		df2 = transformUserInput(df, top_city, CONTINENT_CHOICE)
		c1, c2, c3 = displayCity(df2)
		country1 = db.get_country(c1)
		country2 = db.get_country(c2)
		country3 = db.get_country(c3)

	
	return render_template('results.html', city1=c1 + ',', country1=country1, city2= c2 + ',', country2= country2, city3=c3 + ',', country3=country3)



def transformUserInput(df, top_city_list, continent):
	

	if len(top_city_list) >= 1:
		df['favorite_city_one'] = top_city_list[0]
	else:
		df['favorite_city_one'] = np.nan
	if len(top_city_list) >= 2:
		df['favorite_city_two'] = top_city_list[1]
	else:
		df['favorite_city_two'] = np.nan
	if len(top_city_list) >= 3:
		df['favorite_city_three'] = top_city_list[2]
	else:
		df['favorite_city_three'] = np.nan
	if len(top_city_list) >= 4:
		df['favorite_city_four'] = top_city_list[3]
	else:
		df['favorite_city_four'] = np.nan
	if len(top_city_list) == 5:
		df['favorite_city_five'] = top_city_list[4]
	else:
		df['favorite_city_five'] = np.nan


	df.drop(columns=['topcity', 'continent'], inplace=True)

	df2 = predict_features.createPredictFeatures(df)

	df3 = predict_features.columnSelection(df2)
	selected = predict_features.citySelection(df3, continent)


	return selected


def displayCity(selected_df):
	
	city1 = selected_df.index[0][1]
	city2 = selected_df.index[1][1]
	city3 = selected_df.index[2][1]
	
	
	return city1, city2, city3





















