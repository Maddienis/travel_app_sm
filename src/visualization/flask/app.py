import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for

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
		cont = request.form.get('continent')
		dict_keys = []
		for city_num in range(len(top_city)):
			dict_keys.append(city_num)

		city_dict = dict(zip(dict_keys, top_city))
		df2 = transformUserInput(df, top_city)
		print(type(top_city))
		print(df)
	
	return render_template('results.html', tables = [df2.to_html(classes='data')], cols = df2.columns.values, topcity=cont)

	


@app.route('/recommend/<data>')
def recommend(df):

	return "WORK OKAY"


def transformUserInput(df, top_city_list):
	

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


	return df
















