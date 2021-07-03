import PySimpleGUI as sg
import requests


def getData(userInput):
    APPID = 'da055e0fdcebcdd212402b9b81768fab'
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={zipCode}&APPID={appid}'
    url = url.format(appid=APPID, zipCode=userInput)
    r = requests.get(url).json()
    return r


def convertTemp(kTemp):
    fTemp = ((kTemp - 273.15) * (9 / 5) + 32)
    fTemp = round(fTemp, 2)
    return fTemp


entButton = sg.Button('ENTER', bind_return_key=True)
layout1 = [[sg.Text('Enter Zip Code')], [sg.Input()], [entButton]]
window1 = sg.Window('Weather App', layout1, return_keyboard_events=True)
zipCode = ''

while True:
    event, values = window1.read()
    if event == 'ENTER' or event == sg.WIN_CLOSED:
        zipCode = values[0]
        break
window1.close()

json = getData(zipCode)

coord = json['coord']
weather = json['weather']
main = json['main']
wind = json['wind']
clouds = json['clouds']['all']
name = json['name']

id = weather[0]['id']
weather_main = weather[0]['main']
description = str(weather[0]['description'])
icon = weather[0]['icon']

temp = convertTemp(main['temp'])
feels_like = convertTemp(main['feels_like'])
pressure = main['pressure']
humidity = main['humidity']
temp_min = convertTemp(main['temp_min'])
temp_max = convertTemp(main['temp_max'])

iconUrl = f'https://openweathermap.org/img/wn/{icon}@2x.png'
iconImageResponse = requests.get(iconUrl)

iconImage = sg.Image(data=iconImageResponse.content)

print(weather_main)
layout2 = [[sg.Text("Currently in " + name), sg.Text(description.capitalize())],
           [sg.Text('Temperature: ' + str(temp)), iconImage],
           [sg.Text('Real Feel: ' + str(feels_like))],
           [sg.Text('High: ' + str(temp_min)), sg.Text('Low: ' + str(temp_max))],
           [sg.Text('Humidity: ' + str(humidity) + '%')],
           [sg.Text('Air Pressure: ' + str(pressure) + ' hPa')],
           [sg.Text('Cloudiness: ' + str(clouds) + '%')]
           ]

window2 = sg.Window('Current Weather', layout2)
window2.read()
x = sg.theme_list()
print(x)
