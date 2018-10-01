# Will Wagner
# IST303 Fall 2018
# 9/27/2018
# Week 4 Individual Exercise - Pytest

# This is an individual exercise. Submit a file named multi.py to Canvas. The program does the following:

# 1.	Creates a 12*12 multiplication table (). The table is held in memory in a nested list multi_table, where
# •	multi_table[0][0] holds “X”
# •	The first row holds the number i for every position i
# •	The first column holds the number j for every position j
# •	each product i*j is stored in position multi_table[i][j].

# 2.	Write 3 tests to test your code using pytest.

j_row = ['X', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multi_table = [j_row]


def test_header():
    assert multi_table[0][5] == 5


for row in range(1, 13):
    j_row = [row]

    for column in range(1, 13):
        j_row.append(column*row)

    multi_table.append(j_row)
    j_row = [row+1]


def test_multiplication():
    assert 4*7 == multi_table[4][7]


def test_00():
    assert multi_table[0][0] == 'X'


def Multiply(i, j):
    return multi_table[i][j]


def Make_Table():
    print()
    print(f"{' {:^79} '.format('    12 x 12 Multiplication Table     ')}")
    print(f"{' {:-^79}'.format('')}")
    for row in range(len(multi_table)):
        for column in multi_table[row]:
            print(f"{' | {:>3}'.format(column)}", end='')
        print(' |')
        print(f"{' {:-^79}'.format('')}")


def MainMenu():
    print()
    print('        12x Main Menu')
    print('=============================')
    print()
    print('1 - Multiply')
    print('2 - Show Table')
    print('0 - Quit')


while True:

    MainMenu()
    print()
    menuChoice = input('Menu Choice: ')
    if menuChoice == "1":
        print()
        ii, jj = [int(x)
                  for x in input("Enter i j (1-12 seperated by a space or tab): ").split()]
        print(str(ii) + ' x ' + str(jj) + ' = ' + str(Multiply(ii, jj)))
        print('\n')
    elif menuChoice == "2":
        Make_Table()
    else:
        break
