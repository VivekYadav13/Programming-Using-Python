'''
Another series that can calculate pi is the Nilakantha series. It is a little more complicated to calculate, but gets close to pi much faster than does the Gregory- Leibniz series of Exercise 9. The Nilakantha series is:
PI = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) − 4/(8*9*10) ...
Calculate the first 15 terms of this series. How many digits of pi are correct?
'''

import math


def nilkantha(number):
    val = 3
    j = 3
    for i in range(number):
        val += (((-1)**i)*4)/((i+j-1)*(i+j)*(i+j+1))
        j += 1
    return val


n = int(input("Enter number of terms: "))
print("The value of pi using Nilakantha series for",
      n, "terms is:", nilkantha(n), "\nDifference from original value of pi is of:", nilkantha(n)-math.pi)
