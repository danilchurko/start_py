import uuid
import datetime


class BankAcc(object):
    def __init__(self, name='No Name', uid=uuid.uuid4()):
        self.name_acc = name
        self.id_acc = uid
        self.balance = 0.00
        self.transactions = []

    def set_name(self, user):
        self.name_acc = user

    def deposit(self, val):
        self.balance += val - (val * 0.01)
        self.transactions.append([val, 'COMMISSION - {}'.format(val * 0.01), 'DEP', datetime.datetime.now() \
                                 .strftime("%d.%m.%Y %HH:%MM:%SS")])

    def withdrawal(self, val):
        if self.balance > 0 and self.balance - val >= 0:
            self.balance -= val - (val * 0.01)
            self.transactions.append([val, 'COMMISSION - {}'.format(val * 0.01), 'WIT', datetime.datetime.now() \
                                     .strftime("%d.%m.%Y %HH:%MM:%SS")])
        else:
            print('Enougth funds :(')

    def show_balance(self):
        balanse = 0
        for transactions in self.transactions:
            if 'DEP' in transactions:
                balanse += transactions[0] - (transactions[0] * 0.01)
            elif 'WIT' in transactions:
                balanse -= transactions[0] + (transactions[0] * 0.01)
        return print(balanse)


user = 'Danil C.H.'
acc = BankAcc()
acc.set_name(user)
print(acc.name_acc, acc.id_acc)

acc.deposit(5000)
acc.show_balance()

acc.withdrawal(250)
acc.show_balance()

print(acc.transactions)
