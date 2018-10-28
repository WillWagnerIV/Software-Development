import pytest


SumS = 0
ls = []



def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not prime")
            print(i, " x ", num//i, " = ", num)
            return False
    return True


@pytest.fixture
def SevenPrimes():

    numPrimes = 7
    primeCnt = 2

    while len(ls) < numPrimes:
        if isPrime(primeCnt):
            ls.append (primeCnt)
        primeCnt += 1

    print(ls)
    print(str(sum(ls)))
    return ls


def test_Seven_Sum(SevenPrimes):
    theList = SevenPrimes()[0:]
    theSum = sum(theList)

    assert theSum == 58


test_Seven_Sum(SevenPrimes)
