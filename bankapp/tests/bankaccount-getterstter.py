# Will Wagner
# IST303


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
        self.__name = name
        self.__balance = balance
        self.cDate = creation_date
        try:
            self.cDate < date.today()
        except Exception:
            print ('Creation Date can not be in the future.')
        if self.cDate > date.today():
            self.cDate = "None"

        print(name, id, self.cDate, balance)

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    @name.setter
    def name(self, name):
        self.__name = name

    @balance.setter
    def balance(self, amount):
        self.__balance = amount
        
    @balance.setter
    def set_balance(self, amount):
        self.__balance = amount

    @balance.setter
    def deposit(self, amount):
        self.__balance += amount

    @classmethod
    def countAccounts(cls):
        return cls.count


# Create Savings Account Class using Inheritance
class SavingsAccount(BankAccount):
    def __init_subclass__(self):
        print("Added a Savings Account")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def withdraw(self, amount):
        print("Amount =" + str(amount), self.balance)
        print('Creation Date: ' + str(self.cDate))
        if self.cDate != "None":
            if amount <= self.balance:
                print('Balance Check Passed')
                if self.cDate <= date_today - relativedelta(months=+6):
                    print('Date Check Passed')
                    self.set_balance = self.balance - amount

        print("Amount =" + str(amount), self.balance)

# Create Checking Account Class using Inheritence
class CheckingAccount(BankAccount):
    def __init_subclass__(self):
        print("Added a Checking Account")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def withdraw(self, amount):
        print("Amount =" + str(amount), self.balance)
        if amount >= self.balance:
            self.set_balance = self.balance - (amount + 30)
            print("Amount =" + str(amount), self.balance)
        else:
            self.set_balance = self.balance - amount
            print("Amount =" + str(amount), self.balance)






def CreateTestAccounts():
    
    # Make Some Manual Accounts Once
    curChecking = CheckingAccount('Will Checking Tester', 'ctest01', date_today, 100)
    curSavings = SavingsAccount('Will Savings Tester', 'stest01', date_today, 100)
    pastSavings = SavingsAccount('Will Savings Tester', 'stest02', date_past, 100)
    futureSavings = SavingsAccount('Will Savings Tester', 'stest03', date_future, 100)
    curBank = BankAccount('Will Bank Tester', 'btest01', date_today, 100)
    testSAccount3 = SavingsAccount('Will Savings Tester', 'stest03', date.today(), 100)

    # Add them to the list
    testAccounts = [
        curChecking ,
        curSavings ,
        pastSavings ,
        futureSavings ,
        curBank ,
        testSAccount3
    ]
    return testAccounts

# Create the test Accounts
testAccounts = CreateTestAccounts()

def Valid_Date(acct):
    
        if (acct.cDate == "None"):
            assert str(acct.cDate) == "None"
            print("ran and None")
        else:
            assert acct.cDate <= date.today()
            print("ran and Good Date")

for acct in testAccounts:
        print (acct)
        Valid_Date(acct)