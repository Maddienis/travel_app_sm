
from flask import Flask, render_template, jsonify, request

application = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


@application.route('/')
def index():
	return render_template('index.html')



