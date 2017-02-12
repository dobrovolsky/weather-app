import json
import urllib.request as request
import datetime


class Weather:
    def __init__(self):
        self.api_key = '&APPID=9b804c03cd199973cd5a9a98b80b0f10'
        self.units = '&units=metric'

    def get_weather(self, city: str, data: dict = None):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={0}{1}'.format(city, self.units)
        query = request.urlopen(url + self.api_key).read().decode('utf-8')
        query_json = json.loads(query)
        weather = {}
        weather['temperature'] = query_json['main']['temp']
        weather['humidity'] = str(query_json['main']['humidity']) + '%'
        weather['wind'] = str(query_json['wind']['speed']) + ' km/h'
        weather['sun_rise'] = datetime.datetime.fromtimestamp(query_json['sys']['sunrise']).strftime('%H:%M:%S')
        weather['sun_set'] = datetime.datetime.fromtimestamp(query_json['sys']['sunset']).strftime('%H:%M:%S')
        weather['pressure'] = str(query_json['main']['pressure']) + ' hPa'
        weather['weather'] = str(query_json['weather'][0]['main'])
        if data is dict:
            return weather
        weather_string = '{0}°C {1} {2} {3} sun rise: {4}, sun set: {5}'.format(weather['temperature'],
                                                                                weather['pressure'],
                                                                                weather['wind'],
                                                                                weather['humidity'],
                                                                                weather['sun_rise'],
                                                                                weather['sun_set'])
        return weather_string

    def get_weather_on_days(self, city: str, days: int, data: list = None):
        url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&mode=json{1}&cnt={2}'.format(city,
                                                                                                        self.units,
                                                                                                        days)
        query = request.urlopen(url + self.api_key).read().decode('utf-8')
        query_json = json.loads(query)
        if data is list:
            return query_json['list']
        weather_list = []
        for day in query_json['list']:
            humidity = str(day['humidity']) + '%'
            pressure = str(day['pressure']) + ' hPa'
            temperature = {'day': day['temp']['day'],
                           'evening': day['temp']['eve'],
                           'morning': day['temp']['morn'],
                           'night': day['temp']['night'],
                           'min': day['temp']['min'],
                           'max': day['temp']['max']}
            date = datetime.datetime.fromtimestamp(day['dt']).strftime('%d-%m')
            wind = str(day['speed']) + ' km/h'
            weather = str(day['weather'][0]['main'])
            weather_list.append('{2}: min: {0}, max: {1} {3}'.format(temperature['min'], temperature['max'], date,
                                                                     (weather, pressure, humidity, wind)))
        return weather_list
