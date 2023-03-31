'''
Write a function that takes an integer n and returns a random integer with exactly n digits. For instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because that is really 93, which is a two-digit number.
'''

from random import randint


def randomnum(n):
    s = ''
    while (n > 0):
        if n == 1:
            s += str(randint(1,9))
        else:
            s += str(randint(0,9))
        n -= 1
    return s


a = int(input('Enter number of digits: '))
print('Random', a, 'digit number is', int(randomnum(a)))
