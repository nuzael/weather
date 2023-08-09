from django.shortcuts import render
from datetime import date, timedelta
import requests


def index(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        
        location_name = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={q}&appid=b2f471a92a2e7b7bb4f94ff1d8d1c845')
        lat = location_name.json()[0].get('lat')
        lon = location_name.json()[0].get('lon') 
        
        # r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=b2f471a92a2e7b7bb4f94ff1d8d1c845&lang=pt_br&units=metric')
        
        # weather_main = r.json()['weather'][0]['main']
        # weather_description = r.json()['weather'][0]['description']
        # weather_icon = r.json()['weather'][0]['icon']
        # print(weather_main)
        # print(weather_description)
        # print(weather_icon)
        
        r = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=b2f471a92a2e7b7bb4f94ff1d8d1c845&lang=pt_br&units=metric')
        
        
        # weather_main = r.json()['list'][0]['weather'][0]['main']
        # weather_description = r.json()['list'][0]['weather'][0]['description']
        # weather_icon = r.json()['list'][0]['weather'][0]['icon']
        
        ###############
        today = date.today()
        
        days_api = {
            'first_day': {
                'max_temp': 30,
                'min_temp': 10,
                'avg_temp': 20,
                'weather': [
                    {'hora': '10:00', 'current_temp': 21, 'icon': 'icn.png'},
                    {'hora': '12:00', 'current_temp': 21, 'icon': 'icn.png'}, 
                    {'hora': '14:00', 'current_temp': 21, 'icon': 'icn.png'}, 
                    {'hora': '16:00', 'current_temp': 21, 'icon': 'icn.png'}, 
                    {'hora': '18:00', 'current_temp': 21, 'icon': 'icn.png'}, 
                    {'hora': '20:00', 'current_temp': 21, 'icon': 'icn.png'}, 
                    {'hora': '22:00', 'current_temp': 21, 'icon': 'icn.png'}, 
                    {'hora': '00:00', 'current_temp': 21, 'icon': 'icn.png'},
                ]
            },
            
            'second_day': {},
            'third_day': [],
            'fourth_day': [],
            'fifth_day': [],
            'sixth_day': [],
        }
        
        avg_temp = 0
        max_temp = 0
        min_temp = 0
        count = 0
        for num, day in enumerate(days_api):    
            for item in r.json()['list']:
                # Retorna o Y/M/D
                delta_time = item['dt_txt'][:10]
                
                # Separa as informações para os próximos 5 dias
                if delta_time == str(today + timedelta(days=1)):
                    if count == 0:
                        max_temp = item['main']['temp']
                        min_temp = item['main']['temp']
                        
                    if item['main']['temp'] > max_temp:
                        max_temp = item['main']['temp']
                    elif item['main']['temp'] < min_temp:
                        min_temp = item['main']['temp']
                        
                    count += 1
                    avg_temp += item['main']['temp']
                    
                    
            
        # for item in r.json()['list']:
        #     # Retorna o Y/M/D
        #     delta_time = item['dt_txt'][:10]
            
            # Separa as informações para os próximos 5 dias
            # if delta_time == str(today + timedelta(days=1)):
            #     if count == 0:
            #         max_temp = item['main']['temp']
            #         min_temp = item['main']['temp']
                    
            #     if item['main']['temp'] > max_temp:
            #         max_temp = item['main']['temp']
            #     elif item['main']['temp'] < min_temp:
            #         min_temp = item['main']['temp']
                    
            #     count += 1
            #     avg_temp += item['main']['temp']
                
            # days_api['second_day'] = {'max_temp': max_temp, 'min_temp': min_temp}
                
            # if delta_time == str(today + timedelta(days=2)):
            #     if count == 0:
            #         max_temp = item['main']['temp']
            #         min_temp = item['main']['temp']
                    
            #     if item['main']['temp'] > max_temp:
            #         max_temp = item['main']['temp']
            #     elif item['main']['temp'] < min_temp:
            #         min_temp = item['main']['temp']
                    
            #     count += 1
            #     avg_temp += item['main']['temp']
                
            # days_api['third_day'] = {'max_temp': max_temp, 'min_temp': min_temp}
        #     elif delta_time == str(today + timedelta(days=3)):
        #         days_api['fourth_day'].append([item['main']['temp'], item['weather'][0]['main']])
        #     elif delta_time == str(today + timedelta(days=4)):
        #         days_api['fifth_day'].append([item['main']['temp'], item['weather'][0]['main']])
        #     elif delta_time == str(today + timedelta(days=5)):
        #         days_api['sixth_day'].append([item['main']['temp'], item['weather'][0]['main']])

        # print(main_temp)
        # days_api['first_day'] = {'main_temp': main_temp, 'weather': weather}
        
        # for day in days_api:
        #     print(f'{days_api[day]}\n')
            
        
        # count = 0
        # for weather_info in days:
        #     if count == 0:
        #         weather['avg_temp'] = 0
        #         weather['max_temp'] = weather_info[0]
        #         weather['min_temp'] = weather_info[0]
                
        #     weather['avg_temp'] += weather_info[0]
        #     count += 1
            
        #     if weather_info[0] > weather['max_temp']:
        #         weather['max_temp'] = weather_info[0]
        #     elif weather_info[0] < weather['min_temp']:
        #         weather['min_temp'] = weather_info[0]   
        # else:
        #     weather['avg_temp'] = weather['avg_temp'] / count
            
        # print(weather)
        
        # count = 0
        # for a, b, c, d, e in zip(second_day, third_day, fourth_day, fifth_day, sixth_day):
        #     if count == 0:
                
            
            
        # print(f'Dia 2: {second_day} \n')
        # print(f'Dia 3: {third_day} \n')
        # print(f'Dia 4: {fourth_day} \n')
        # print(f'Dia 5: {fifth_day} \n')
        # print(f'Dia 6: {sixth_day} \n')
        
    context = {
        'a': 's'
    }   
    return render(request, 'core/index.html', context=context)