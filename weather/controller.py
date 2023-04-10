from app import db
from .models import Weather
import requests

class WeatherController:
    @staticmethod
    def get_weather(lat, lon):
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=<api_key>&units=metric'
        response = requests.get(url).json()
        return response

    @staticmethod
    def get_weathers():
        return Weather.query.all()

