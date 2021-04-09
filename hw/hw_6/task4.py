import json
import datetime

duration = []


def listsum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + listsum(num_list[1:])


def open_file():
    with open('acdc.json', 'r') as file:
        dict_json = json.load(file)

        with open('acdc.json') as file_temp:
            total = sum(1 for line in file_temp.readlines() if 'duration' in line)
            # print(total)

        for i in range(total):
            duration_temp = dict_json['album']['tracks']['track'][i]['duration']
            duration.append(int(duration_temp))

        json.dumps(dict_json)
        sum_sec = listsum(duration)
        print(f'Total duration: {sum_sec} sec.')

        sum_time = datetime.timedelta(0, sum_sec, 0)
        print(f'Total duration: {sum_time} min.')


open_file()
