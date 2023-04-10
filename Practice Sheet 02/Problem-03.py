'''
Calculate an approximation to pi. There is an infinite series called the Gregory-Leibniz series that sums to pi. Of course it can never reach the exact value because there is no such thing, but it can compute as many digits as are desired. The series is:
PI = 4/1-4/3 + 4/5 - 4/7 + 4/9 - 4/11....
Write a program that calculates the result of the first 15 terms of this series. How many digits of pi are correct? Add six more terms. How many digits are correct now?
'''

import math


def gregory_leibniz(number):
    val = 0
    for i in range(number):
        val += (((-1)**i)*4)/((2*i)+1)
    return val


n = int(input("Enter number of terms: "))
print("The value of pi using Gregory-Leibniz series for",
      n, "terms is:", gregory_leibniz(n), "\nDifference from original value of pi is of:", gregory_leibniz(n)-math.pi)
