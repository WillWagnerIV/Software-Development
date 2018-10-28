uTime = date.today()
lTime = date.today()
pTime = date(2017, 5, 15)
fTime = lTime + relativedelta(months=+6)

# print(uTime.strftime("%c"))
# print(lTime.strftime("%c"))
# print(uTime - lTime)

testCAccount = CheckingAccount('Will Checking Tester', 'ctest01', uTime, 100)
testSAccount = SavingsAccount('Will Savings Tester', 'stest01', uTime, 100)
testSAccount2 = SavingsAccount('Will Savings Tester', 'stest02', pTime, 100)
testSAccount3 = SavingsAccount('Will Savings Tester', 'stest03', fTime, 100)
testBAccount = BankAccount('Will Bank Tester', 'btest01', uTime, 100)

@pytest.fixture
def TestAccounts():
    uTime = date.utcnow()
    lTime = date.now()
    pTime = date(2017, 5, 15)
    fTime = date.utcnow() + relativedelta(months=+6)

    curChecking = CheckingAccount('Will Checking Tester', 'ctest01', uTime, 100)
    curSavings = SavingsAccount('Will Savings Tester', 'stest01', uTime, 100)
    pastSavings = SavingsAccount('Will Savings Tester', 'stest02', pTime, 100)
    futureSavings = SavingsAccount('Will Savings Tester', 'stest03', fTime, 100)
    curBank = BankAccount('Will Bank Tester', 'btest01', uTime, 100)

    return futureSavings


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

print (testAccounts[0].creation_date)
def test_Valid_Date(acct):
    
        if (acct.creation_date == "None"):
            assert str(acct.creation_date) == "None"
            print("ran and None")
        else:
            assert acct.creation_date <= date.today()
            print("ran and Good Date")

@pytest.fixture
def acct():
    for Bacct in testAccounts:
        print (Bacct)
        test_Valid_Date(Bacct)

        

def test_Valid_Date(TestAccounts):

    if (TestAccounts.cDate == "None"):
        assert str(TestAccounts.cDate) == "None"
        print("ran and None")
    else:
        assert TestAccounts.cDate <= date.today()
        print("ran and Good Date")


def test_Savings_Withdrawl():

    t3 = SavingsAccount('Will Savings Tester', 'stest02', pTime, 100)
    t3.withdraw = 50

    assert t3.view_balance == 50


def test_Savings_Overdraft():

    t3 = SavingsAccount('Will Tester', 'stest02', pTime, 100)
    t3.withdraw = 200

    assert t3.view_balance == 100


def test_Checking_Withdrawl():

    t3 = CheckingAccount('Will Tester', 'stest02', pTime, 100)
    t3.withdraw = 50

    assert t3.view_balance == 50


def test_Checking_Overdraft():

    t3 = CheckingAccount('Will Tester', 'stest02', pTime, 100)
    t3.withdraw = 200

    assert t3.view_balance == -130


def test_Savings_Deposit():

    t3 = SavingsAccount('Will Tester', 'stest02', pTime, 100)
    t3.deposit = 100

    assert t3.view_balance == 200


def test_Checking_Deposit():

    t3 = CheckingAccount('Will Savings Tester', 'stest02', pTime, 100)
    t3.deposit = 100

    assert t3.view_balance == 200
