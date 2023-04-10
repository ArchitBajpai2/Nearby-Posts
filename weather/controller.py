from app import db
from .models import Weather
import requests

class WeatherController:
    @staticmethod
    def get_weather(lat, lon):
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8adc7fc8e661496be8711a7d2a4dae05&units=metric'
        response = requests.get(url).json()
        return response

    @staticmethod
    def get_weathers():
        return Weather.query.all()

