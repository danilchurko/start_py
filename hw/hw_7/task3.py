import requests
import datetime
from benchmark import benchmark


# @benchmark(iters=10)
def make_predict_txt(cnt, q):
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt={}&units=metric&appid' \
      '=f9ada9efec6a3934dad5f30068fdcbb8'.format(q, cnt)

    response = requests.get(url).json()
    date_start = datetime.datetime.fromtimestamp(response['list'][0]['dt']).strftime("%d-%m-%Y")

    f = open('{}-{}-{}-days-weather-forecast.txt'.format(date_start, q, cnt), 'w')
    f.write('Date\t\t\t' + 'Temp DAY\t\t' + 'Feels like DAY\t\t' + 'Temp NIGHT\n')

    for day in response['list']:
        temp_day = day['temp']['day']
        temp_night = day['temp']['night']
        temp_feel = day['feels_like']['day']

        date_start = datetime.datetime.fromtimestamp(day['dt']).strftime("%d-%m-%Y")
        f.write(
            '{0}\t\t{1}\t\t\t{2}\t\t\t\t{3}\n'.format(str(date_start), str(temp_day), str(temp_feel), str(temp_night)))


cnt = input('Count of days (max 17): ')
q = input('City: ')

make_predict_txt(cnt, q)
