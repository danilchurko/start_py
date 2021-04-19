import requests
import datetime
from benchmark import benchmark

API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'


def user_input():
    cnt = input('Count of days (max 17): ')
    q = input('City: ')
    return cnt, q


# @benchmark(iters=10)
def make_predict_txt(cnt, q):
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?',
                            params={'q': q, 'cnt': cnt, 'units': 'metric', 'appid': API_KEY}).json()

    date_start = datetime.datetime.fromtimestamp(response['list'][0]['dt']).strftime("%d-%m-%Y")

    with open('{}-{}-{}-days-weather-forecast.txt'.format(date_start, q, cnt), 'w') as f:
        f.write('Date\t\t\t' + 'Temp DAY\t\t' + 'Feels like DAY\t\t' + 'Temp NIGHT\n')

        for day in response['list']:
            temp_day = day['temp']['day']
            temp_night = day['temp']['night']
            temp_feel = day['feels_like']['day']

            date_start = datetime.datetime.fromtimestamp(day['dt']).strftime("%d-%m-%Y")
            f.write(
                '{0}\t\t{1}\t\t\t{2}\t\t\t\t{3}\n'.format(str(date_start), str(temp_day),
                                                          str(temp_feel), str(temp_night)))


def main():
    cnt, q = user_input()
    make_predict_txt(cnt, q)


if __name__ == '__main__':
    main()
