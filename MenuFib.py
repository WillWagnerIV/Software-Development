# Will Wagner
# IST303
# 9/8/2018
# Menu Driven Fibonacci Generators

'''
 The definition with Fib(0) = 1 is known as the combinatorial definition, and Fib(0) = 0 is the classical definition. 
 Both are used in the Fibonacci Quarterly, though authors that use the combinatorial definition need to add a sentence of explanation. 
 Benjamin and Quinn in Proofs that Really Count use f_n for the nth combinatorial Fibonacci number 
 and F_n for the nth classical Fibonacci number. 
 The combinatorial definition is good, not surprisingly for counting questions like 
 "How many ways are there to walk up a flight of n steps, taking either one or two steps at a time?" 
 When n is 0, there's one way to do it, not zero ways.
 --Dale Gerdemann
'''


# Initialize Variables
mainLooping = True


#  Generate Fibonacci numbers - Basic Method  
def NoListFib (n):

    firNum = 0
    secNum = 1
    i = 0

    print()
    print ('The first '+ n + ' Fibonacci numbers are:')
    print (secNum) # Combinatorial definition 0 is not a Fib number

    while i < int(n)-1:
        fib = firNum + secNum
        print (fib)
        firNum = secNum
        secNum = fib
        i += 1


#  Generate Fib numbers and save in a List
def ListFib (n):

    firNum = 0
    secNum = 1
    i = 0

    fibList = [1]

    while i < int(n)-1:
        fib = firNum + secNum
        fibList.append(fib)
        firNum = secNum
        secNum = fib
        i += 1

    print ('The first ' + n + ' Fibonacci numbers are: ' + str(fibList) )


#  Generate Fib numbers using List Slices instead of variables
def ListNoVar (n):

    fibList = [0,1]

    while len(fibList) < int(n)+1:
        fibList.append(fibList[-1]+fibList[-2])

    print ('The first ' + n + ' Fibonacci numbers are: ' + str(fibList[1:]) )


#  Generate Fib numbers using recursion
def RecursiveFib (n):

    n = int(n)

    if n <= 1:
        return n
    else:
       return(RecursiveFib(n-1) + RecursiveFib(n-2))


#  Print the results of the recursive function
def ShowRFib(n):

    print("The first " + n + " numbers in the Fibonacci sequence:")
    for i in range(int(n)):
       print(RecursiveFib(i))



#  Main Menu
def MainMenu():
    print ()
    print ('       ###   Main Menu   ###')
    print ()
    print (' 1 - No List')
    print (' 2 - List at End')
    print (' 3 - List Slices instead of Variables')
    print (' 4 - Recursion <--- Important! ')
    print (' 0 - Quit')
    print ()
    

#  Main Loop
while (mainLooping):

    ''' 
    A very basic Main Menu.  
    With two of the simplest error checking methods.
    '''

    MainMenu()
    menuChoice = input (' Selection: ')

    if menuChoice in ("1","2","3","4"):
        print()
        n = input('How many Fibbonacci numbers? ')

    if menuChoice == '0':
        mainLooping = False
        break

    elif menuChoice == '1':
        NoListFib(n)

    elif menuChoice == '2':
        ListFib(n)

    elif menuChoice == '3':
        ListNoVar(n)

    elif menuChoice == '4':
        ShowRFib(n)  #  Note that this calls a function to show the results of the recursive function
                     #  It does not call the recursive version directly
    else:
        print ()
        print ('Please choose one of the options above.')
        print ()


    

    