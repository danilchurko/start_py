from datetime import date


def is_date(day, month, year):
    if date(year, month, day):
        return True
    else:
        return False


print(is_date(14, 4, 2021))
print(is_date(29, 2, 2018))
