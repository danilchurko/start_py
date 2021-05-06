import argparse
import csv
import sys


def check_args_4name():
    for key in list(args_dict):
        value = args_dict[key]
        if value is None or key == 'o':
            del args_dict[key]

    return args_dict


def check_args(row):
    dict_args = {k: v for k, v in args_dict.items() if v is not None}
    if not dict_args:
        sys.exit(0)

    save_flag = False
    map_dict = {
        'brand': 'BRAND',
        'color': 'COLOR',
        'year': 'MAKE_YEAR',
        'fuel': 'FUEL',
        'reg_num': 'N_REG_NEW'
    }

    for k, v in dict_args.items():
        if row[map_dict[k]] == v:
            save_flag = True
        else:
            save_flag = False

    return save_flag


def make_filename():
    name_file = ''
    temp_list = []

    for key in args_for_name:
        value = args_for_name[key]
        if key == 'o':
            continue
        elif key == 'reg_num':
            temp_list.append('reg_num+')
        else:
            temp_list.append(value)

    name_file = name_file + '-'.join(temp_list) + ".csv"
    return name_file


def open_csv():
    result = []
    with open('tz_opendata.csv', 'r+') as File:
        csv_reader = csv.DictReader(File, delimiter=';')

        for row in csv_reader:
            if check_args(row):
                result.append(row)

    save_csv(result, fieldnames)


def save_csv(result, fieldnames):
    with open(make_filename(), "w+", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        for row in result:
            writer.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='CAR DATA 1.0', description='Know car data')
    parser.add_argument('o', default='tz_opendata.csv', type=str)
    parser.add_argument('--brand', type=str)
    parser.add_argument('--year', type=str)
    parser.add_argument('--fuel', type=str)
    parser.add_argument('--color', type=str)
    parser.add_argument('--reg_num', type=str)

    args = parser.parse_args()

    if args.reg_num == 'yes':
        fieldnames = ['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'FUEL', 'N_REG_NEW']
    else:
        fieldnames = ['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'FUEL']

    args_dict = vars(args)

    args_for_name = check_args_4name()

    print(args_for_name)
    print(args_dict)
    print(make_filename())

    open_csv()
