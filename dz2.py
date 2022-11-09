#Задание для самостоятельного решения: Вывести скорость ветра и видимость для текущего прогноза и для прогноза на неделю
import requests

city = "Moscow, RU"
appid = "07df54970140a8e6c0160e19b889c1d5"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data1 = res.json()

print("Прогноз ветра и видимости на сегодня:")
print('Cкорость ветра: ', data1['wind']['speed'], ' м/с')
print("Видимость: ", (data1['visibility'] / 10000)*100, '%')
print('----------------------------------')

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data2 = res.json()

print("Прогноз ветра и видимости на неделю:")
for i in data2["list"]:
    print("Дата: ", i['dt_txt'],
    "\r\n Скорость ветра: ", i['wind']['speed'], ' м/с',
    "\r\n Видимость: ", round((i['visibility'] / 10000)*100), '%')