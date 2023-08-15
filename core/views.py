from django.shortcuts import render
from datetime import date, timedelta
from django.shortcuts import redirect
import requests
import os

from dotenv import load_dotenv
load_dotenv()

appid = os.getenv('API_KEY') 

def index(request):
    current_weather = get_current_weather('Rio de Janeiro')
    forecast_weather = get_forecast_weather('Rio de Janeiro')
    
    if request.method == 'GET':
        city_name = request.GET.get('q')
        if city_name == '':
            return redirect('index')
        
        if city_name != None:
            current_weather = get_current_weather(city_name)
            forecast_weather = get_forecast_weather(city_name)
        
    context = {
        'current_weather': current_weather,
        'forecast_weather': forecast_weather,
    }   
    return render(request, 'core/index.html', context=context)

def get_city_location(city_name):
    location_name = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={appid}')
    
    location = {
        'lat': location_name.json()[0].get('lat'),
        'lon': location_name.json()[0].get('lon'),
    }
    
    return location

def get_current_weather(city_name):

    location = get_city_location(city_name)
    
    r_current_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location['lat']}&lon={location['lon']}&appid={appid}&lang=pt_br&units=metric")   
    
    # Checking if it's raining
    if r_current_weather.json().get('rain'):
        if r_current_weather.json().get('rain').get('3h'):
            rain_value = r_current_weather.json()['rain']['3h']
        else:
            rain_value = r_current_weather.json()['rain']['1h']
    else:
        rain_value = 0
    
    # Current weather information
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
    
    return current_weather

def get_forecast_weather(city_name):
    
    location = get_city_location(city_name)
    
    r_forecast_weather = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={location['lat']}&lon={location['lon']}&appid={appid}&lang=pt_br&units=metric")
    
    forecast_weather = [
        {
            'day': 'second',
            'temp': [],
            'max_temp': 0,
            'min_temp': 0,
            'icon': 0,
        },
        {
            'day': 'third',
            'temp': [],
            'max_temp': 0,
            'min_temp': 0, 
            'icon': 0,
        },
        {
            'day': 'fourth',
            'temp': [],
            'max_temp': 0,
            'min_temp': 0,
            'icon': 0,
        },
        {
            'day': 'fifth',
            'temp': [],
            'max_temp': 0,
            'min_temp': 0,
            'icon': 0,
        },
        {
            'day': 'sixth',
            'temp': [],
            'max_temp': 0,
            'min_temp': 0,  
            'icon': 0, 
        },
    ]
    
    for item in r_forecast_weather.json()['list']:
        # Return Y/M/D  
        delta_time = item['dt_txt'][:10]
        
        # Separates data for each day
        if str(date.today() + timedelta(days=0)) == delta_time:
            pass
        
        elif str(date.today() + timedelta(days=1)) == delta_time:
            forecast_weather[0]['temp'].append(item['main']['temp'])
            forecast_weather[0]['max_temp'] = round(max(forecast_weather[0]['temp']))
            forecast_weather[0]['min_temp'] = round(min(forecast_weather[0]['temp']))
            if int(forecast_weather[0]['icon']) < int(item['weather'][0]['icon'][:2]):
                if int(forecast_weather[0]['icon']) < 10:
                    forecast_weather[0]['icon'] = item['weather'][0]['icon'][:2]
                else:
                    forecast_weather[0]['icon'] = item['weather'][0]['icon'][:2]
            
        elif str(date.today() + timedelta(days=2)) == delta_time:
            forecast_weather[1]['temp'].append(item['main']['temp'])
            forecast_weather[1]['max_temp'] = round(max(forecast_weather[1]['temp']))
            forecast_weather[1]['min_temp'] = round(min(forecast_weather[1]['temp']))
            if int(forecast_weather[1]['icon']) < int(item['weather'][0]['icon'][:2]):
                if int(forecast_weather[1]['icon']) < 10:
                    forecast_weather[1]['icon'] = item['weather'][0]['icon'][:2]
                else:
                    forecast_weather[1]['icon'] = item['weather'][0]['icon'][:2]
            
        elif str(date.today() + timedelta(days=3)) == delta_time:
            forecast_weather[2]['temp'].append(item['main']['temp'])
            forecast_weather[2]['max_temp'] = round(max(forecast_weather[2]['temp']))
            forecast_weather[2]['min_temp'] = round(min(forecast_weather[2]['temp']))
            if int(forecast_weather[2]['icon']) < int(item['weather'][0]['icon'][:2]):
                if int(forecast_weather[2]['icon']) < 10:
                    forecast_weather[2]['icon'] = item['weather'][0]['icon'][:2]
                else:
                    forecast_weather[2]['icon'] = item['weather'][0]['icon'][:2]
            
        elif str(date.today() + timedelta(days=4)) == delta_time:
            forecast_weather[3]['temp'].append(item['main']['temp'])
            forecast_weather[3]['max_temp'] = round(max(forecast_weather[3]['temp']))
            forecast_weather[3]['min_temp'] = round(min(forecast_weather[3]['temp']))
            if int(forecast_weather[3]['icon']) < int(item['weather'][0]['icon'][:2]):
                if int(forecast_weather[3]['icon']) < 10:
                    forecast_weather[3]['icon'] = item['weather'][0]['icon'][:2]
                else:
                    forecast_weather[3]['icon'] = item['weather'][0]['icon'][:2]
            
        elif str(date.today() + timedelta(days=5)) == delta_time:
            forecast_weather[4]['temp'].append(item['main']['temp'])
            forecast_weather[4]['max_temp'] = round(max(forecast_weather[4]['temp']))
            forecast_weather[4]['min_temp'] = round(min(forecast_weather[4]['temp']))
            if int(forecast_weather[4]['icon']) < int(item['weather'][0]['icon'][:2]):
                if int(forecast_weather[4]['icon']) < 10:
                    forecast_weather[4]['icon'] = item['weather'][0]['icon'][:2]
                else:
                    forecast_weather[4]['icon'] = item['weather'][0]['icon'][:2]
        else:
            break
        
    return forecast_weather