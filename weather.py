import requests
import re
import json
from urllib.request import urlopen


def get_weather(city, country):
	city = city
	country = country
	api_key = "626121804677a747d341262c3a0a2ac4"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	url = base_url + "appid=" + api_key + "&q=" + city
	kelvin = 273.15
	response = requests.get(url)
	response_json = response.json()
	x = response_json['main']
	temperature = x['temp']
	temp_c = temperature - kelvin
	real_temp = x['feels_like']
	real_temp_c = real_temp - kelvin
	humidity = x['humidity']
	w = response_json['wind']
	wind = round(w['speed']* 1.852)
	z = response_json['weather'][0]
	sky = z['description']
	print('Right now the sky is', sky[0:5])
	print("The temperature is ", round(temp_c), "degrees celsium")
	print('The real feel is ', round(real_temp_c), "degrees celsium")
	print('The humidity is ', humidity,'%')
	print('The speed of the wind is ', wind, 'km/h')

def get_city():
	url = 'http://ipinfo.io/json'
	response = urlopen(url)
	data = json.load(response)
	city = data['city']
	country = data['country']
	print("You live in " + city + ', ' + country)
	get_weather(city, country)


get_city()