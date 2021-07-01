
import json
import requests

class OpenWeatherMap:
    APPID = 'da055e0fdcebcdd212402b9b81768fab'

    def __init__(self):
        self.url = 'https://api.openweathermap.org/data/2.5/weather?zip={zipCode}&APPID={appid}'
        self.json = {}

    def getZipcode(self):
        url = self.url.format(appid=OpenWeatherMap.APPID,zipCode=input('Enter Zip Code '))
        self.json = requests.get(url).json()
        return self.json

    def K2F(kTemp):
        fTemp = ((kTemp-273.15)*(9/5)+32)
        fTemp = round(fTemp,2)
        return fTemp

    def loadWeather(self):
        
        weatherData = self.json
        w = weatherData['weather']
        tempData = (weatherData['main'])

        locName = weatherData['name']
        wState = w[0]['main']
        wDescrip = (w[0]['description']).capitalize()
        curTemp = OpenWeatherMap.K2F(tempData['temp'])
        realFeel = OpenWeatherMap.K2F(tempData['feels_like'])
        lowTemp = OpenWeatherMap.K2F(tempData['temp_min'])
        highTemp = OpenWeatherMap.K2F(tempData['temp_max'])
        humidity = tempData['humidity']

        print('Current weather in %s:'%(locName))
        print(wState,':',wDescrip)
        print('Temp:', curTemp)
        print('Humidity:',humidity,'%')
        print('Feels like:',realFeel)
        print('High:',highTemp,'| Low:', lowTemp)

x = OpenWeatherMap()
x.getZipcode()
x.loadWeather()
