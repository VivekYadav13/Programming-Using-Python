'''
Write a function called number_of_factors that takes an integer and returns how many factors the number has and print all factors.
'''

def number_of_factors(n):
    factors = []
    number = 0
    for i in range(1, n+1):
        if n % i == 0:
            factors += [i]
            number += 1
    return factors, number


a = int(input("Enter a positive integer: "))
print("The given number has", number_of_factors(a)[
      1], "factors which are", number_of_factors(a)[0])
