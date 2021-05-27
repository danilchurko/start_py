import random
import pprint


class City:
    def __init__(self):
        self.streets = []

    def gen_str(self):
        for i in range(random.randint(0, 10)):
            self.streets.append(Street(i))

    @property
    def population(self):
        population = 0
        for street in self.streets:
            for house in street.houses:
                population += house.people

        return population

    def fin_list(self):
        finlist = []
        for street in self.streets:
            for house in street.houses:
                finlist.append([street.idd, house.idd, house.people])

        return finlist


class Street:
    def __init__(self, idd):
        self.houses = []
        self.gen_hous()
        self.idd = idd

    def gen_hous(self):
        for i in range(random.randint(5, 20)):
            self.houses.append(House(i))


class House:
    def __init__(self, idd):
        self.people = random.randint(1, 100)
        self.idd = idd


odessa = City()
odessa.gen_str()
print('Population: {}'.format(odessa.population))
pprint.pprint(odessa.fin_list())
