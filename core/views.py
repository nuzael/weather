from django.shortcuts import render
from datetime import date, timedelta
import requests
import os

from dotenv import load_dotenv
load_dotenv()

appid = os.getenv('API_KEY')

def index(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        
        location_name = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={q}&appid={appid}')
        lat = location_name.json()[0].get('lat')
        lon = location_name.json()[0].get('lon') 

        r_current_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}&lang=pt_br&units=metric')   
        
        r_forecast_weather = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={appid}&lang=pt_br&units=metric')
        
        
        if r_current_weather.json().get('rain'):
            if r_current_weather.json().get('rain').get('3h'):
                rain_value = r_current_weather.json()['rain']['3h']
            else:
                rain_value = r_current_weather.json()['rain']['1h']
        else:
            rain_value = 0
            
        current_weather = {
            'current_temp': round(r_current_weather.json()['main']['temp']),
            'icon': f"https://openweathermap.org/img/wn/{r_current_weather.json()['weather'][0]['icon']}@2x.png",
            'city': r_current_weather.json()['name'],
            'feels_like': round(r_current_weather.json()['main']['feels_like']),
            'cloudy': r_current_weather.json()['clouds']['all'],
            'humidity': r_current_weather.json()['main']['humidity'],
            'wind': round(r_current_weather.json()['wind']['speed'] * 3.6), #km/h
            'rain': rain_value,
        }
        
        print(r_forecast_weather.json())
        
    context = {
        'current_weather': current_weather
    }   
    return render(request, 'core/index.html', context=context)