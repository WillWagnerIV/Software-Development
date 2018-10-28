from bankaccount import *
import pytest

#input output values for account with balance $500
input_output = (
    (20, 520),
    (30, 530),
    (-35, 465),
    (12, 512)
)

#parametrized fixture
@pytest.fixture(params=input_output)
def input_output_tuples(request):
    a = BankAccount()
    a.balance = 500
    return (a, request.param)

#test function utilizing parametrized fixture
def test_deposit_advanced(input_output_tuples):
    input_output_tuples[0].deposit(input_output_tuples[1][0])
    assert input_output_tuples[0].balance == input_output_tuples[1][1]


#fixture for creating Account objects
@pytest.fixture()
def create_objects():
    a = BankAccount("X Abc", 1234, date.today(), 500)
    b = CheckingAccount("X Abc", 1234, date.today(), 500)
    c = SavingsAccount("X Abc", 1234, date.today(), 500)
    return [a, b, c]

#test checking account withdraw
def test_checking_withdraw(create_objects):
    create_objects[1].balance = 561
    create_objects[1].withdraw(561)
    assert create_objects[1].balance == 0

#parametrized tests for deposit
@pytest.mark.parametrize("deposited_amount, updated_balance",
                            [
                            (20, 520),
                            (30, 530),
                            pytest.param(-35,465, marks=pytest.mark.xfail(reason="Deposit of negative amount should be disallowed")),
                            pytest.param(10, 512, marks=pytest.mark.xfail(reason="Deposit of $10 on $500 balance must not give a balance of $512"))
                            ]
)
def test_deposit(deposited_amount, updated_balance):
    c = CheckingAccount("X Abc", 1234, date.today(), 500)
    c.deposit(deposited_amount)
    assert c.balance == updated_balance

def test_future_date(create_objects):
    with pytest.raises(Exception):
        a = BankAccount("X Abc", 1234, date.today() + timedelta(days=2), 500)
