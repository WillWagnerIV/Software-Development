import pytest


@pytest.fixture
def firstSevenPrimes():
    return {2,3,5,7,11,13,17}

def test_SumOfPrimes(firstSevenPrimes):
    theSum = 0
    for x in firstSevenPrimes:
        theSum += x

    assert theSum == (2+3+5+7+11+13+17)