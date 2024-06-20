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
    print("input data:",input_data)

    #url for model
    #url = "http://localhost:5000/api" # use this locally
    url = 'https://climate-change-model-12a504c55e5e.herokuapp.com/api' # for herooku deploy

    # Post data to URL with correct headers
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=input_data, headers=headers)

    # Check for errors in response
    if response.status_code != 200:
        return render_template("index.html", date=date, text=text, results=f"Error: {response.status_code} - {response.content.decode('UTF-8')}")

    response_data = response.json()

    # Send input values and prediction result to index.html for display
    return render_template("index.html", date=date, text=text, results=response_data)

    #post data to url
    #results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    #return render_template("index.html", date = date, text = text, results=results.content.decode('UTF-8'))
  
