from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/tweet_eval", methods=['GET', 'POST'])
def tweet_eval():

    #extract form inputs
    date = request.form.get("date")
    text = request.form.get("text")

    #convert data to json
    input_data = json.dumps({"date": date, "text": text})

    #url for model
    url = "http://localhost:5000/api" # use this locally
    #url = "https://bank-model-app.herokuapp.com/api" 
    #url = "https://car-eval-model-cdd5c766580c.herokuapp.com/api"

    #post data to url
    results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    return render_template("index.html", date = date, text = text, results=results.content.decode('UTF-8'))
  
