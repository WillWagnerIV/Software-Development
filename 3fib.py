import numpy

x = 0
y = 1

i = 0

s = input('How many Fibbonacci numbers? ') 

print (y)

while i < int(s)-1:
    fib = x + y
    print (fib)
    x = y
    y = fib
    i += 1