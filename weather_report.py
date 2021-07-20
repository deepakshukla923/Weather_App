import requests
import os
from datetime import date, datetime

my_api = os.environ["weather_api"]
location = input("Enter the city name: ")

complete_link = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + my_api
api_link = requests.get(complete_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid City: {}, Please check your City name".format(location))
else:
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    humid = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("----------------------------------------------------------")
    print(f"Weather Stats for - {location.upper()} || {date_time}")
    print("----------------------------------------------------------")
    print("Current temperature is       : {:.2f} deg C".format(temp_city))
    print("Current weather description  :", weather_desc)
    print("Current Humidity             :", humid, '%')
    print("Current wind speed           :", wind_speed, 'kmph')
