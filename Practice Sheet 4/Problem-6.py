"""Not complete"""
from random import randint


def randomnum(n):
    s = ''
    while (n > 0):
        s += str(randint(0, 9))
        n -= 1
    return s


a = int(input('Enter number of digits: '))
print('Random ', a, ' digit number is ', int(randomnum(a)))
