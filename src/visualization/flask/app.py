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
		print(req)

		homecountry = request.form["homeCountry"]
		age = request.form["age"]
		gender = request.form["gender"]

		print(homecountry)

		return redirect(request.url)

	return render_template('starter_template_new.html')

def featureClean(user_input):

	return

@app.route('/handle_data', methods=['POST'])
def handle_data():
	projectpath = request.form['projectFilepath']

	return projectpath