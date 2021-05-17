import uuid
import datetime


class BankAcc(object):
    name_acc = str()
    id_acc = str(uuid.uuid4())
    balance = float()
    transactions = []

    def __init__(self, name='No Name', uid=uuid.uuid4()):
        self.name_acc = name
        self.id_acc = uid
        self.balance = 0.00
        self.trans = []

    def deposit(self, val):
        self.balance += val - (val * 0.01)
        self.transactions.append([val, 'COMMISSION - {}'.format(val * 0.01), 'DEPOSIT', datetime.datetime.now() \
                                 .strftime("%d.%m.%Y %HH:%MM:%SS")])

    def withdrawal(self, val):
        self.balance -= - val - (val * 0.01)
        self.transactions.append([val, 'COMMISSION - {}'.format(val * 0.01), 'WITHDRAWAL', datetime.datetime.now() \
                                 .strftime("%d.%m.%Y %HH:%MM:%SS")])

    def show_balance(self):
        return print(round(self.balance, 5))


acc = BankAcc()
print(acc.name_acc, acc.id_acc)

acc.deposit(5000)
acc.show_balance()

acc.withdrawal(250)
acc.show_balance()

print(acc.transactions)
