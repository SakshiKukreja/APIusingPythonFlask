from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def introduction():
    return 'Try \'/weater/\' for weather report'

@app.route('/weather/', methods = ['GET'])
def weather():
    city = request.args['city']
    apiKey = request.args['apiKey'] 

    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'q': city, 'appid': apiKey})
    return response.json()

if __name__ == "__main__":
    app.run()