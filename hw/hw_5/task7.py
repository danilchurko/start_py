from datetime import date


def is_date(day, month, year):
    try:
        date(year, month, day)
        return True
    except:
        return False


print(is_date(41, 4, 2021))
print(is_date(11, 2, 2018))
