'''
The Goldbach conjecture asserts that every even number is the sum of two prime numbers. Write a program that gets a number from the user, checks to make sure that it is even, and then finds two prime numbers that add up to the number.
'''

def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def goldbach(n):
    for i in range(2, n-1):
        if isprime(i):
            m = n-i
            if isprime(m):
                break
    return i, m


def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False


a = int(input("Enter an even integer: "))
if iseven(a):
    print("According to Goldbach conjecture, sum is:",
          goldbach(a)[0], "+", goldbach(a)[1])
else:
    print("Number is not even")
