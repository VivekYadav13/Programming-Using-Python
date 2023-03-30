"""
Write a function called binom that takes two integers n and k and returns the binomial coefficient.
"""
from math import factorial


def binom(n, k):
    return float(factorial(n)/(factorial(k)*factorial(n-k)))


a, b = int(input('Enter integer n = ')), int(input('Enter integer k = '))
print('The binomial coefficient n!/k!(n-k)! = ', binom(a, b))
