import requests
from flask import Flask
app = Flask(__name__)

API_KEY = '<key>' # OpenWeather API Key
API_URL = 'http://api.openweathermap.org/data/2.5/weather?zip={},us&mode=json&units=imperial&appid={}'

def query_api(zip):
    try:
        data = requests.get(API_URL.format(zip, API_KEY).json())
    except Exception as exc: 
        print(exc)
        data = None
    return data

@app.route('/weather/<zip>')
def result(zip):
    resp = query_api(zip)
    try:
        text = resp["name"] + " temperature is " + str(resp["main"]["temp"]) + " degrees Fahrenheit with " + resp["weather"][0]["description"] + "."
    except:
        text = "There was an error.<br>Did you include a valid U.S. zip code in the URL?"
    return text

if __name__ == '__main__':
    app.run(debug=True)
