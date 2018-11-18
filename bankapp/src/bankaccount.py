# Will Wagner
# IST303

import dateutil
from datetime import date
from dateutil.relativedelta import relativedelta
import pytest

date_today = date.today()
date_past = date_today + relativedelta(months= -6)
date_future = date_today + relativedelta(months= +6)

testAccounts = []

class BankAccount():

    # Class Variables
    count = 0

    def __init__(self, name = "Rumbi Gwanz", id="123", creation_date = date.today() , balance = 0):
        BankAccount.count += 1
        print ()
        print ("Added a Bank Account")

        self.name = name
        self.id = id
        self.balance = balance
        self.creation_date = creation_date

        if self.creation_date > date.today():
            try:
                raise Exception('You may not have a creation date in the future.')
            except Exception as error:
                print(repr(error))
            self.creation_date = "None"

        # print(name, id, self.creation_date, balance)

        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    @classmethod
    def countAccounts(cls):
        return cls.count


# Create Savings Account Class using Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, name, id, creation_date, balance):
        super().__init__(name, id, creation_date, balance)
        print ('Made it a Savings Account')

    def withdraw(self, amount):
        print("Amount =" + str(amount))
        print('Creation Date: ' + str(self.creation_date))
        if self.creation_date != "None":
            if amount <= self.balance:
                print('Balance Check Passed')
                if self.creation_date <= date_today - dateutil.relativedelta(months=+6):
                    print('Date Check Passed')
                    self.set_balance = self.balance - amount

        print("Amount = " + str(amount) + " New Balance: " + self.balance)

# Create Checking Account Class using Inheritence
class CheckingAccount(BankAccount):

    def __init__(self, name, id, creation_date, balance):
        super().__init__(name, id, creation_date, balance)
        print ('Made it a Checking Account')

    def withdraw(self, amount):
        print("Amount =" + str(amount))
        if amount > self.balance:
            self.balance = self.balance - (amount + 30)
            print("Amount = " + str(amount) + " New Balance: " + str (self.balance))
        else:
            self.balance = self.balance - amount
            print("Amount = " + str(amount) + " New Balance: " + str (self.balance))


curChecking = CheckingAccount('Will Checking Tester', 'ctest01', date_today, 100)
curSavings = SavingsAccount('Will Savings Tester', 'stest01', date_today, 100)
pastSavings = SavingsAccount('Will Savings Tester', 'stest02', date_past, 100)
futureSavings = SavingsAccount('Will Savings Tester', 'stest03', date_future, 100)
curBank = BankAccount('Will Bank Tester', 'btest01', date_today, 100)
testSAccount3 = SavingsAccount('Will Savings Tester', 'stest03', date.today(), 100)


