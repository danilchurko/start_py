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

        # with open('acdc.json') as file_temp:
        #     total = sum(1 for line in file_temp.readlines() if 'duration' in line)
        #     # print(total)

        # если один цикл, то как вычислить сколько раз нужно его выполнять?
        # чтобы range() сам выставлялся в зависимости от кол-ва треков
        for i in range(10):
            duration_temp = dict_json['album']['tracks']['track'][i]['duration']
            duration.append(int(duration_temp))

        # in sec
        sum_sec = listsum(duration)
        print(f'Total duration: {sum_sec} sec.')

        # *timedelta
        sum_time = datetime.timedelta(0, sum_sec, 0)
        print(f'Total duration: {sum_time} min.')


open_file()
