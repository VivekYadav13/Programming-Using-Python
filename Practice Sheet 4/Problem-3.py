'''
Write a function called sum_digits that is given an integer num and returns the sum of the digits of num.
'''

def sum_digit(n):
    s = 0
    while (n > 0):
        r = n % 10
        s = s+r
        n = int(n/10)
    return s


num = int(input("Input positive integer number: "))
print("Sum of digits of ", num, "= ", sum_digit(num))
while (num > 0):
    print("Sum of digits of ", num, "= ", sum_digit(num))
    num = int(input("Input positive integer number: "))
