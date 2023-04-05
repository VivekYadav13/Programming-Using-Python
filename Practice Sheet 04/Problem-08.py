'''
Our number system is called base 10 because we have ten digits: 0, 1, . . . , 9. Some cultures, including the Mayans and Celts, used a base 20 system. In one version of this system, the 20 digits are represented by the letters A through T. Here is a table showing a few conversions:
Write a function called base20 that converts a base 10 number to base 20. It should return the result as a string of base 20 digits. One way to convert is to find the remainder when the number is divided by 20, then divide the number by 20, and repeat the process until the number is 0. The remainders are the base 20 digits in reverse order, though you have to convert them into their letter equivalents.
'''

def base20(n):
    s = ''
    while n > 0:
        r = n % 20
        n = int(n / 20)
        ch = chr(65 + r)
        s = ch + s
    return s


number = int(input("Enter a number in base 10: "))
print(base20(number))
