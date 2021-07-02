import requests


def convertTemp(kTemp):
    fTemp = ((kTemp - 273.15) * (9 / 5) + 32)
    fTemp = round(fTemp, 2)
    return fTemp


class OpenWeatherMap:
    APPID = 'da055e0fdcebcdd212402b9b81768fab'

    # locName = ''
    # wState = ''
    # wDescription = ''
    # curTemp = ''
    # realFeel = ''
    # lowTemp = ''
    # highTemp = ''
    ##humidity = ''

    def __init__(self, tempData=None, weatherData=None, w=None, userInput=None):
        self.url = 'https://api.openweathermap.org/data/2.5/weather?zip={zipCode}&APPID={appid}'
        url = self.url.format(appid=OpenWeatherMap.APPID, zipCode=userInput)
        self.json = requests.get(url).json()
        # return self.json
        self.locName = weatherData['name']
        self.wState = w[0]['main']
        self.wDescription = (w[0]['description']).capitalize()
        self.curTemp = convertTemp(tempData['temp'])
        self.realFeel = convertTemp(tempData['feels_like'])
        self.lowTemp = convertTemp(tempData['temp_min'])
        self.highTemp = convertTemp(tempData['temp_max'])
        self.humidity = tempData['humidity']
        #self.url = 'https://api.openweathermap.org/data/2.5/weather?zip={zipCode}&APPID={appid}'
        # self.json = {}

    def dataSend(self):
        return None

    # def getZipcode(self, userInput):
    #     url = self.url.format(appid=OpenWeatherMap.APPID, zipCode=userInput)
    #     self.json = requests.get(url).json()
    #     return self.json

    def printWeather(self):
        print('Current weather in %s:' % (self.locName))
        print(self.wState, '->', self.wDescription)
        print('Temp:', self.curTemp)
        print('Humidity:', self.humidity, '%')
        print('Feels like:', self.realFeel)
        print('High:', self.highTemp, '| Low:', self.lowTemp)
