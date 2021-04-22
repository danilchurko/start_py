import argparse
import csv


def read_csv():
    results = []
    with open('tz_opendata.csv', 'r+') as File:
        reader = csv.DictReader(File, delimiter=';')
        for line in reader:
            if args.brand is None and args.year is None and args.fuel is None and args.color is None:
                break
            elif line["BRAND"] == str.upper(args.brand) and line["MAKE_YEAR"] == str.upper(args.year) and \
                    line["FUEL"] == str.upper(args.fuel) and line["COLOR"] == str.upper(args.color):
                results.append(line)
                # print(line)

    return results


def write_csv(fieldnames, data):
    with open('BRAND-{}-YEAR-{}-FUEL-{}-COLOR-{}.csv'.format(args.brand, args.year, args.fuel, args.color), "w+",
              newline='') \
            as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        for row in data:
            writer.writerow(row)
    print('~~~DONE~~~')


def main():
    result = read_csv()

    if args.reg_num == 'yes':
        fieldnames = ['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'FUEL', 'N_REG_NEW']
    else:
        fieldnames = ['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'FUEL']

    temp_list = []

    for values in result[1:]:
        inner_dict = dict(zip(fieldnames, values))
        temp_list.append(inner_dict)

    write_csv(fieldnames, result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='CAR DATA 1.0', description='Know car data')
    parser.add_argument('o', default='tz_opendata.csv', type=str)
    parser.add_argument('--brand', type=str)
    parser.add_argument('--year', type=str)
    parser.add_argument('--fuel', type=str)
    parser.add_argument('--color', type=str)
    parser.add_argument('--reg_num', type=str)

    args = parser.parse_args()
    # print(args)
    main()
