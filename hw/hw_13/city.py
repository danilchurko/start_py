import random
from pprint import pprint


class City:
    def __init__(self):
        self.street = [Street() for i in range(random.randint(5, 10))]


class Street:
    def __init__(self):
        self.houses = [House() for i in range(random.randint(5, 20))]

        for i in range(random.randint(5, 20)):
            self.houses = i


class House:
    def __init__(self):
        self.population = random.randint(1, 100)


def full_city():
    finlist = []
    for strt in City().street:
        for hous in Street().houses:
            people = House().population
            finlist.append([strt, hous, people])

    return finlist


def print_city():
    print('Улица', 'Дом', 'Население')
    pprint(full_city())


print_city()
