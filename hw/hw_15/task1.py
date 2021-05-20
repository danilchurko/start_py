import re
import csv

a = input('Enter your vehicle number: ')
a.replace('I', 'І', 2)

pattern = r'^\w{2}\d{4}\w{2}'
matches = re.search(pattern, a)

if not matches:
    print('No it\'s not a car number')
else:
    print('Pass')
    with open('ua_auto.csv', newline='') as File:
        reader = csv.DictReader(File)

        for row in reader:
            if a[0:2] == row['Код 2004']:
                print('2004 for', row['Регіон'])
                break
            elif a[0:2] == row['Код 2013']:
                print('2013 for', row['Регіон'])
                break
