import random
from pprint import pprint


class City:
    street = random.randint(5, 10)

    def str_list(self):
        streetlist = list(range(1, self.street))
        return streetlist


class Street:
    def __init__(self):
        self.houses = random.randint(5, 20)

    def hous_list(self):
        houselist = list(range(1, self.houses))
        return houselist


class House:
    def __init__(self):
        self.population = random.randint(1, 100)


def full_city():
    finlist = []
    for street in City().str_list():
        for house in Street().hous_list():
            people = House().population
            finlist.append([street, house, people])

    return finlist


def print_city():
    print('Улица', 'Дом', 'Население')
    pprint(full_city())


print_city()
