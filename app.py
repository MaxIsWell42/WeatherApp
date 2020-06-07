from flask import Flask, render_template, request
import requests
import json
import os

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def homepage():
    if request.method == "POST":
        city = request.form("City Name: ")
        state = request.form("State Code: ")
    
    params = {
    'api_key': os.environ.get('API_KEY'),
    'city_name': city,
    'state_code': state,
    }
    
    r = requests.get(
        'api.openweathermap.org/data/2.5/weather?q={city_name},{state_code}&appid={API_KEY}',
        params=params)
    print(r.url, "hello")
    
    return render_template('weatherHome.html', weather=r) # Add name of JSON catagory we're looking for

if __name__ == '__main__':
    app.run()