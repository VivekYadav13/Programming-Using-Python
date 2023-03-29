"""
The digital root of a number n is obtained as follows: Add up the digits n to get a new number. Add up the digits of that to get another new number. Keep doing this until you get a number that has only one digit. That number is the digital root.
For example, if n = 45893, we add up the digits to get 4 + 5 + 8 + 9 + 3 = 29.
We then add up the digits of 29 to get 2 + 9 = 11. We then add up the digits of 11 to get 1 + 1 = 2. Since 2 has only one digit, 2 is our digital root.
Write a function that returns the digital root of an integer n.
"""
def sum_digit(n):
    s = 0
    while (n > 0):
        r = n % 10
        s = s+r
        n = int(n/10)
    return s


def digital_root(num):
    while (num > 9):
        num = sum_digit(num)
        return (num)


num = int(input("Input positive integer number: "))
print("Sum of digits of ", num, "= ", sum_digit(num))
while (num > 0):
    print("Digital root of ", num, "= ", sum_digit(num))
    num = int(input("Input positive integer number: "))
