import datetime

from weather import Weather

weather = Weather()
while True:
    city = input('Enter city: ')
    days = input('Enter days: ')
    weather_data = weather.get_weather(city)
    print(weather_data)

    weather_data = weather.get_weather_on_days(city, days)
    for item in weather_data:
        print(item)
    if input('If you want to see another city enter (y)') != 'y':
        break
