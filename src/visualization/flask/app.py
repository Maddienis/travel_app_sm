import pandas as pd
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# Can add /home or leave it. 
@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		#Can delete this
		req = request.form

		top_city = request.form.getlist('topcity')

		print(top_city)
		d = request.form.to_dict()
		df = pd.DataFrame([d])
		print(df)
		print(type(df))


		return redirect(request.url, req=req)
	return render_template('starter_template_new.html')

def featureSelect(user_input):

	return

@app.route('/handle_data', methods=['POST'])
def handle_data():
	projectpath = request.form['projectFilepath']

	return projectpath