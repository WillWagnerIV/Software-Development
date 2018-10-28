# Will Wagner
# IST303
# 9/14/2018


ls = []

# Determine if Prime - don't need all the factorials, just enough to determine not prime


def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not prime")
            print(i, " x ", num//i, " = ", num)
            return False

    return True


# Main Code
numPrimes = int(input("How many Primes? "))

if numPrimes < 1:
    print(' Please choose an integer greater than 0.')
else:

    primeCnt = 2

    while len(ls) < numPrimes:

        if isPrime(primeCnt):
            ls.append(primeCnt)

        primeCnt += 1


print(ls)
