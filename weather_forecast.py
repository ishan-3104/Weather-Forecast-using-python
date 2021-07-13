#Weather Forecast code

import requests
from datetime import datetime

#fatch the data from website
user_api = "235b4cb2a254f15e423eb3519a3a5cd8"
city_name = input("Enter City Name : ")
api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+user_api
api_link_f = requests.get(api_link)
api_data = api_link_f.json()

#check city name is valide or not
if api_data['cod']=='404':
    print(f"Invalid City : {city_name},please check your City name.")
else:
    city_temp = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    wind_speed = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    print("*"*60)
    print(f"Weather status for {city_name} || {date_time}")
    print("*"*60)
    print(f"Current Temprature is : {city_temp:.2f} deg C")
    print(f"Current Weather desc is : {weather_desc}")
    print(f"Current wind speed is : {wind_speed} kmph")
    print("*"*60)