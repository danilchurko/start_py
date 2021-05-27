import re
import csv

a = input('Enter your vehicle number: ')
a.replace('I', 'І', 2)

patt = r'^\w{2}\d{4}\w{2}'
match = re.search(patt, a)

if not match:
    print('ERROR')
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
