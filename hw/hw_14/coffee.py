import csv


class Product:
    def __init__(self, name, ttype, coast):
        self.name = name
        self.type = ttype
        self.coast = coast


class Store:
    with open('inventory.csv', 'r+') as File:
        csv_reader = csv.DictReader(File, delimiter=',')

        for row in csv_reader:
            Product.name = row['Name']
            Product.type = row['Type']
            Product.coast = row['Coast']


print(Product)
