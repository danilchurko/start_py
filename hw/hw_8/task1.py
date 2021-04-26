import json
import argparse
import requests
from datetime import datetime, timedelta
from pprint import pprint

today = datetime.now()
result = [['Date', 'From', 'To', 'Amount', 'Rate', 'Result']]


def get_symbols():
    with open('symbols.json', 'r') as file:
        dict_json = json.load(file)
        curr_symbols = dict_json['symbols']
    return curr_symbols


def make_request():
    curr_symbols = get_symbols()
    if args.fr in curr_symbols and args.to in curr_symbols:
        if args.start_date != today:
            start_date = datetime.strptime(args.start_date, "%Y-%m-%d")

            while start_date < today:
                response = requests.get('https://api.exchangerate.host/convert',
                                        params={'from': args.fr, 'to': args.to,
                                                'amount': args.amount, 'date': start_date}).json()

                result.append([str(response['date']), str(response['query']['from']), str(response['query']['to']),
                               str(response['query']['amount']), str(response['info']['rate']), str(response['result'])])

                start_date += timedelta(days=1)
    else:
        print('Currency name NOT FOUND. Try AGAIN')
    pprint(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Online curensy exchange 2.0', description='Know currency at your time')
    parser.add_argument('fr', default='USD', type=str)
    parser.add_argument('to', default='UAH', type=str)
    parser.add_argument('amount', default=100.00, type=float)
    parser.add_argument('--start_date', default=today)

    args = parser.parse_args()
    # print(args)
    make_request()



