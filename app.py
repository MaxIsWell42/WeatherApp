from flask import Flask, render_template, request
import requests
import json
import os

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def homepage():
    # Get the API key
    api_key = os.environ.get('API_KEY')
    
    # Some default values
    city = "San Francisco"
    state = "CA"
    
    # If a location has not been submitted yet, ask for one(WIP)
    if request.method == "POST":
        city = request.form("City Name: ")
        state = request.form("State Code: ")
    
    # params = {
    # 'city_name': city,
    # 'state_code': state,
    # 'api_key': os.environ.get('API_KEY'),
    # }
    # print(params['api_key'])
    
    # Make the request
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'
    r = requests.get(
        url.format(city, state, api_key)).json()
    # print("\n", r.url, "\n")
    
    return render_template('base.html', weather=r) # Add name of specific JSON category if you want one

if __name__ == '__main__':
    app.run()