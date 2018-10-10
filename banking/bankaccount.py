"""
    Create a class called BankAccount in a file called bankaccount.py and upload to Canvas:

    The class is initialized with the owner’s name (name), alphanumeric ID (id),
        date of creation (creation_date), and balance.
        The date of creation can be the current date or a past date, but not a date in the future.
        If the creation date is not valid, creation_date should point to None.
    It has 3 methods: deposit(amount), withdraw(amount), and view_balance().
    It has a class variable, count, which tracks the number of accounts that have been created
    There are two subclasses to BankAccount: a Savings account and a Checking account.

    Savings
    only allows withdrawals after 6 months has passed since the creation of the account.
    Does not allow overdrafts.
    Checking
    allows overdraft, but adds a $30 penalty fee each time a withdrawal results in a negative balance.

    Write the following tests for the class in the same file:

    A test for the BankAccount constructor, to ensure that date of creation is valid
    A test for the Savings account withdrawal, to ensure it updates the balance correctly
    A test for the Savings account withdrawal, to ensure it doesn’t allow negative balances
    A test for the Checking account withdrawal, to ensure it updates the balance correctly
    A test for the Checking account withdrawal, ensuring that the right balance is calculated
        after a withdrawal resulting in an overdraft

"""

from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import pytest


class BankAccount():

    # Class Variables
    count = 0

    uTime = datetime.utcnow()
    lTime = datetime.now()
    pTime = datetime(2017, 5, 15)
    fTime = datetime.utcnow() + relativedelta(months=+6)

    def __init__(self, name, id, creation_date, balance):
        BankAccount.count += 1
        self.__name = name
        self.__balance = balance
        self.cDate = creation_date
        if self.cDate > datetime.utcnow():
            self.cDate = "None"

        print(name, id, self.cDate, balance)

    @property
    def name(self):
        return self.__name

    @property
    def view_balance(self):
        return self.__balance

    @name.setter
    def name(self, name):
        self.__name = name

    @view_balance.setter
    def set_balance(self, amount):
        self.__balance = amount

    @view_balance.setter
    def deposit(self, amount):
        self.__balance += amount

    @classmethod
    def countAccounts(cls):
        return cls.count


class Savings(BankAccount):

    def __init_subclass__(self):
        print("Added a Savings Account")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def withdraw(self, amount):
        print("Amount =" + str(amount), self.view_balance)
        print('Creation Date: ' + str(self.cDate))
        if self.cDate != "None":
            if amount <= self.view_balance:
                print('Balance Check Passed')
                if self.cDate <= uTime - relativedelta(months=+6):
                    print('Date Check Passed')
                    self.set_balance = self.view_balance - amount

        print("Amount =" + str(amount), self.view_balance)


class Checking(BankAccount):
    def __init_subclass__(self):
        print("Added a Checking Account")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def withdraw(self, amount):
        print("Amount =" + str(amount), self.view_balance)
        if amount >= self.view_balance:
            self.set_balance = self.view_balance - (amount + 30)
            print("Amount =" + str(amount), self.view_balance)
        else:
            self.set_balance = self.view_balance - amount
            print("Amount =" + str(amount), self.view_balance)


uTime = datetime.utcnow()
lTime = datetime.now()
pTime = datetime(2017, 5, 15)
fTime = datetime.utcnow() + relativedelta(months=+6)

print(uTime.strftime("%c"))
print(lTime.strftime("%c"))

print(uTime - lTime)

testCAccount = Checking('Will Checking Tester', 'ctest01', uTime, 100)
testSAccount = Savings('Will Savings Tester', 'stest01', uTime, 100)
testSAccount2 = Savings('Will Savings Tester', 'stest02', pTime, 100)
testSAccount3 = Savings('Will Savings Tester', 'stest03', fTime, 100)
testBAccount = BankAccount('Will Bank Tester', 'btest01', uTime, 100)


# testSAccount2.conTest()


# x = uTime - cTime
# print('SA2 Creation Date: ' + cTime.strftime("%c"))

# if cTime <= uTime - relativedelta(months=+6):
#     print('Older than 6 months')


def test_Valid_Date():

    t3 = Savings('Will Savings Tester', 'stest03', fTime, 100)

    if (t3.cDate == "None"):
        assert str(t3.cDate) == "None"
        print("ran and None")
    else:
        assert t3.cDate <= datetime.utcnow()
        print("ran and Good Date")


def test_Savings_Withdrawl():

    t3 = Savings('Will Savings Tester', 'stest02', pTime, 100)
    t3.withdraw = 50

    assert t3.view_balance == 50


def test_Savings_Overdraft():

    t3 = Savings('Will Tester', 'stest02', pTime, 100)
    t3.withdraw = 200

    assert t3.view_balance == 100


def test_Checking_Withdrawl():

    t3 = Checking('Will Tester', 'stest02', pTime, 100)
    t3.withdraw = 50

    assert t3.view_balance == 50


def test_Checking_Overdraft():

    t3 = Checking('Will Tester', 'stest02', pTime, 100)
    t3.withdraw = 200

    assert t3.view_balance == -130


def test_Savings_Deposit():

    t3 = Savings('Will Tester', 'stest02', pTime, 100)
    t3.deposit = 100

    assert t3.view_balance == 200


def test_Checking_Deposit():

    t3 = Checking('Will Savings Tester', 'stest02', pTime, 100)
    t3.deposit = 100

    assert t3.view_balance == 200
