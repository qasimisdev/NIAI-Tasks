# Task 27 - user defined exceptions

class NegativeAmountError(Exception):
    pass


class NotEnoughMoneyError(Exception):
    def __init__(self, balance, wanted):
        self.balance = balance
        self.wanted = wanted
        super().__init__(f"balance is {balance} but you asked for {wanted}")


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError("can't deposit a negative amount")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError("can't withdraw a negative amount")
        if amount > self.balance:
            raise NotEnoughMoneyError(self.balance, amount)
        self.balance -= amount


acc = Account(500)

try:
    acc.deposit(200)
    print("balance:", acc.balance)
    acc.withdraw(1000)
except NotEnoughMoneyError as e:
    print("failed:", e)
    print("short by", e.wanted - e.balance)

try:
    acc.deposit(-50)
except NegativeAmountError as e:
    print("failed:", e)

# a simple age check
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("must be 18 or older")
    print("age ok")

for a in (25, 12):
    try:
        check_age(a)
    except InvalidAgeError as e:
        print("age", a, "->", e)
