import re


def telephone():
    a = input('Enter your phone number: ')
    matches = re.search(r'0([- ()]?\d){9}', a)
    if matches:
        print('(+38)', matches.group()[0:3], matches.group()[3:6], '-'
              , matches.group()[6:8], '-', matches.group()[8:10])
    else:
        print('Failed to recognize number')
    return matches.group()


telephone()
