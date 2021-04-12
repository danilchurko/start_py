import requests
import datetime

cnt = input('Count of days (max 17): ')
q = input('City: ')

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt={}&units=metric&appid' \
      '=f9ada9efec6a3934dad5f30068fdcbb8'.format(q, cnt)

response = requests.get(url).json()
date_start = datetime.datetime.fromtimestamp(response['list'][0]['dt']).strftime("%d-%m-%Y")

f = open('{}-{}-{}-days-weather-forecast.txt'.format(date_start, q, cnt), 'w')
f.write('Date\t\t\t' + 'Weater DAY\t\t' + 'DAY Feels like\t\t' + 'Temp NIGHT\n')

for day in response['list']:
    temp_day = day['temp']['day']
    temp_night = day['temp']['night']
    temp_feel = day['feels_like']['day']

    date_start = datetime.datetime.fromtimestamp(day['dt']).strftime("%d-%m-%Y")
    f.write(str(date_start) + '\t\t' + str(temp_day) + '\t\t\t' + str(temp_feel) + '\t\t\t\t' + str(temp_night) + '\n')
