"""
Note to future self: using venv means you have to be in the venv directory...
use flask --app hello run  
"""
import requests
from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal


app = Flask(__name__)

API_KEY = '28cac5439407194a409a227079e0c106' # OpenWeather API Key
API_URL = 'http://api.openweathermap.org/data/2.5/weather?zip={},us&mode=json&units=imperial&appid={}'

presidents_list = convert_to_dict("presidents.csv")

# Helper functions

def query_api(zip):
    try:
        data = requests.get(API_URL.format(zip, API_KEY).json())
    except Exception as exc: 
        print(exc)
        data = None
    return data

## Route functions

@app.route("/")
def hello():
    greet = '<h1>Hello, Gators!</h1>'
    link = '<p><a href="weather/95014">Click me!</a></p>'
    return greet + link

@app.route("/user/<name>")
def user(name):
    return render_template('hello.html', name=name)

@app.route('/weather/<zip>')
def result(zip):
    resp = query_api(zip)
    try:
        text = resp["name"] + " temperature is " + str(resp["main"]["temp"]) + " degrees Fahrenheit with " + resp["weather"][0]["description"] + "."
    except:
        text = "There was an error.<br>Did you include a valid U.S. zip code in the URL?"
    return text

@app.route('/president/<num>')
def detail(num):
    try:
        pres_dict = presidents_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Presidency: {num}</h1>"
    # a little bonus function, imported on line 2 above
    ord = make_ordinal( int(num) )
    return render_template('president.html', pres=pres_dict, ord=ord, the_title=pres_dict['President'])


if __name__ == '__main__':
    app.run(debug=True)
