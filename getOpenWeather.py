APPID = 'da055e0fdcebcdd212402b9b81768fab'

import json
import requests
import sys


def K2F(kTemp):
    fTemp = ((kTemp-273.15)*(9/5)+32)
    fTemp = round(fTemp,2)
    return fTemp

zipCode = input('Enter Zip Code')


url = 'https://api.openweathermap.org/data/2.5/weather?zip=%s&APPID='%(zipCode)+APPID
res = requests.get(url)
res.raise_for_status()

weatherData = json.loads(res.text)
w = weatherData['weather']
tempData = (weatherData['main'])

locName = weatherData['name']
wState = w[0]['main']
wDescrip = w[0]['description']
curTemp = K2F(tempData['temp'])
realFeel = K2F(tempData['feels_like'])
lowTemp = K2F(tempData['temp_min'])
highTemp = K2F(tempData['temp_max'])
humidity = tempData['humidity']

print('Current weather in %s:'%(locName))
print(wState,':',wDescrip)
print('Temp:', curTemp)
print('Humidity:',humidity,'%')
print('Feels like:',realFeel)
print('High:',highTemp,'| Low:', lowTemp)
