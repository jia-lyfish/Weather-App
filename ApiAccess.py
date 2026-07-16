import requests
import os
from datetime import datetime

#First of all, gonna store the api.
user_api = os.environ['weather_api']
location = input("Enter the city name: ")

#pasted from the website: 
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api


#Call the api, use json to store data, and then print the data to interpret it.
api_link = requests.get(complete_api_link)
api_data = api_link.json()


#Storing values in variables

temp_city = int(((api_data['main']['temp']) - 273.15))
feels_like = int(((api_data['main']['feels_like']) - 273.15))
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
vsbl = ((api_data['visibility'])//1000)
wind_spd = api_data['wind']['speed']
sunrise = api_data['sys']['sunrise']
sunset = api_data['sys']['sunset']


date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
