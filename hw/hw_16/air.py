import csv


def user_input():
    user_inp = 0
    chosen_par = input('"iata_code" or "country" or "name": ')

    if chosen_par == 'iata_code':
        chosen_value = input('Iata_code: ')
        user_inp = [chosen_par, chosen_value]

        if len(user_inp[1]) != 3:
            raise NameError('Only 3 letters')
        return user_inp

    elif chosen_par == 'country':
        chosen_value = input('Country: ')
        user_inp = ['iso_country', chosen_value]
        return user_inp

    elif chosen_par == 'name':
        chosen_value = input('Name: ')
        user_inp = [chosen_par, chosen_value]
        return user_inp

    else:
        print('Enougth option')
        return user_inp


with open('airport-codes_csv.csv', encoding='utf8', newline='') as File:
    reader = csv.DictReader(File)
    user_inp = user_input()

    for row in reader:
        if user_inp[0] in list(row.keys()) \
                and user_inp[1] in list(row.values()) \
                and user_inp[0] != 'name':
            with open('result_airport.csv', 'a', encoding='utf8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(row.values())

        elif user_inp[0] in list(row.keys()) \
                and user_inp[0] == 'name' \
                and str(user_inp[1]).lower() in str(row['name'].lower()):

            with open('result_airport.csv', 'a', encoding='utf8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(row.values())
