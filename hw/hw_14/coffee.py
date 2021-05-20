import csv


class Product:
    def __init__(self, name, ttype, price, count):
        self.name = name
        self.ttype = ttype
        self.price = price
        self.count = count

        if ttype != 'coffee' and ttype != 'tea':
            raise NameError('NOT COFFEE OR TEA')

    def show_products(self):
        print(f'{self.name}: {self.ttype},  Цена: {self.price}')

    def get_price(self):
        return self.price

    def get_type(self):
        return self.ttype

    def get_name(self):
        return self.name


class Store:
    def __init__(self):
        self.products = []
        self.cash = 0
        self.count = 5

    def import_products(self):
        with open('inventory.csv', 'r+') as File:
            reader = csv.DictReader(File, delimiter=',')

            for row in reader:
                self.products.append(Product(row.get('Name'), row.get('Type'), row.get('Price'), self.count))

    def show_items(self):
        flag = input('enter \'cof\' or \'tea\' or \'all\' for all:  ')
        for product in self.products:
            if flag == 'cof':
                if Product.get_type(product) == 'coffee':
                    Product.show_products(product)
            elif flag == 'tea':
                if Product.get_type(product) == 'tea':
                    Product.show_products(product)
            else:
                Product.show_products(product)

    def total_cost(self):
        cost = 0
        for product in self.products:
            cost += int(Product.get_price(product))
        return cost

    def sell(self, item):
        for product in self.products:
            if Product.get_name(product) == item:
                self.cash += int(self.products[item].get_price())
                self.count -= 1
                if self.count == 0:
                    del self.products[item]
            else:
                pass


store = Store()
store.import_products()
store.show_items()

print('Total coast all items = {}'.format(store.total_cost()))

store.sell('Американо')
store.sell('Американо')
store.sell('Американо')
store.sell('Американо')
store.sell('Американо')
store.sell('Американо')
store.show_items()
print('Total coast all items = {}'.format(store.total_cost()))

print('In our cashier: ', store.cash)

