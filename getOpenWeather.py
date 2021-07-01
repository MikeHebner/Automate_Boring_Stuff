import requests


def convertTemp(kTemp):
    fTemp = ((kTemp - 273.15) * (9 / 5) + 32)
    fTemp = round(fTemp, 2)
    return fTemp


class OpenWeatherMap:
    APPID = 'da055e0fdcebcdd212402b9b81768fab'

    def __init__(self):
        self.url = 'https://api.openweathermap.org/data/2.5/weather?zip={zipCode}&APPID={appid}'
        self.json = {}

    def getZipcode(self):
        url = self.url.format(appid=OpenWeatherMap.APPID, zipCode=input('Enter Zip Code '))
        self.json = requests.get(url).json()
        return self.json

    def loadWeather(self):
        weatherData = self.json
        w = weatherData['weather']
        tempData = (weatherData['main'])

        locName = weatherData['name']
        wState = w[0]['main']
        wDescription = (w[0]['description']).capitalize()
        curTemp = convertTemp(tempData['temp'])
        realFeel = convertTemp(tempData['feels_like'])
        lowTemp = convertTemp(tempData['temp_min'])
        highTemp = convertTemp(tempData['temp_max'])
        humidity = tempData['humidity']

        print('Current weather in %s:' % (locName))
        print(wState, '->', wDescription)
        print('Temp:', curTemp)
        print('Humidity:', humidity, '%')
        print('Feels like:', realFeel)
        print('High:', highTemp, '| Low:', lowTemp)


while True:
    x = OpenWeatherMap()
    x.getZipcode()
    x.loadWeather()
