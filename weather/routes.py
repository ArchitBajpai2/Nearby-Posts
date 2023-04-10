from flask import Blueprint, jsonify, request
from .controller import WeatherController
from .models import Weather

weather = Blueprint('weather', __name__)

@weather.route('/weather', methods=['GET'])
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    weather = WeatherController.get_weather(lat=lat, lon= lon)
    return jsonify(weather)