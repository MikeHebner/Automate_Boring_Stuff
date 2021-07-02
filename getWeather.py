import requests
import json


def getWeather(userInput):
    APPID = 'da055e0fdcebcdd212402b9b81768fab'
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={zipCode}&APPID={appid}'
    url = url.format(appid=APPID, zipCode=userInput)
    r = requests.get(url).json()
    print(r)

