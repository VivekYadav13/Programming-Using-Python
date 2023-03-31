'''
Write a program that asks the user to enter a value n, and then computes (1 + 1/2 + 1/3 + ... + 1/n) - ln(n) . The ln function is log in the math module.
'''

import math

n = int(input("Enter a positive integer n: "))
a = 0
for b in range(1,n+1):
    a += (1/b)
print("Desired out put is =", str(a-(math.log(n))))
