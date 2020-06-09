from flask import Flask, render_template, request, url_for
from forms import LocationForm
import requests
import json
import os

# Start the Flask app
app = Flask(__name__)

# Generate a CSRF Secret Key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/success', methods=["GET","POST"])
def homepage():
    # Get the API key
    api_key = os.environ.get('API_KEY')
    # print(api_key)
    
    # Some default values
    city = "San Francisco"
    state = "California"
        
    # Make the request
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'
    r = requests.get(
        url.format(city, state, api_key))
    # x = json.loads(r)
    # r = x["weather"]
    weatherJSON = r.json()
    r = weatherJSON["weather"]
    # print("\n", r.json(), "\n")
    
    return render_template('base.html', weather=r) # Add name of specific JSON category if you want one

@app.route("/", methods = ['GET', 'POST'])
def Location():
    form = LocationForm()
    if form.validate_on_submit():
        city = LocationForm.city.data
        state = LocationForm.state.data
        print(city, state)
        return url_for('success')
    return render_template('location.html', form=form)

if __name__ == '__main__':
    app.run()