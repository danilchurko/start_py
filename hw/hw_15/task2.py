import re

phh = input('Enter your number: ')


def telephone(phph):
    ph = phph
    matches = re.search(r'0([- ()]?\d){9}', ph)
    if matches:
        print('(+38)', matches.group()[0:3], matches.group()[3:6], '-'
              , matches.group()[6:8], '-', matches.group()[8:10])
    else:
        print('ERROR')
    return matches.group()


telephone()
