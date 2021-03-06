import json
import datetime

from benchmark import benchmark

duration = []


def listsum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + listsum(num_list[1:])


@benchmark
def open_file():
    with open('acdc.json', 'r') as file:
        dict_json = json.load(file)

        duration_temp = dict_json['album']['tracks']['track']
        for track in duration_temp:
            duration.append(int(track['duration']))

        duration_temp = dict_json['album']['tracks']['track']
        for track in duration_temp:
            print(track['@attr'], track['name'])

        # in sec
        sum_sec = listsum(duration)
        print(f'Total duration: {sum_sec} sec.')

        # timedelta
        sum_time = datetime.timedelta(0, sum_sec, 0)
        print(f'Total duration: {sum_time} min.')


open_file()
