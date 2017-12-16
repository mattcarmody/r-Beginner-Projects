#!/usr/bin/python3
# proj23WhatsTheWeather.py - r/BeginnerProjects #23
# https://www.reddit.com/r/beginnerprojects/comments/1dzbu7/project_whats_the_weather/
# Daily forecasts now require a paid API key, so output is adjusted from the problem set

import json
import requests
import sys

url = "http://api.openweathermap.org/data/2.5/forecast?zip=ZIPCODEHERE,us&APPID=efd82d96b2b21b943a240a31758ae37d"
weatherJSON = requests.get(url)
try:
	weatherJSON.raise_for_status()
except:
	print("Something went wrong getting the API data")
	sys.exit()
	
weatherDict = json.loads(weatherJSON.text)

print("Current Weather:")
print(str(round(weatherDict["list"][0]["main"]["temp"]-273.15, 1)) + " degrees Celsius.")
print(weatherDict["list"][0]["weather"][0]["main"])
for i in range(1, 5):
	print()
	print(str(i*24) + " hours from now:")
	print(str(round(weatherDict["list"][i*8]["main"]["temp"]-273.15, 1)) + " degrees Celsius.")
	print(weatherDict["list"][i*8]["weather"][0]["main"])
	
