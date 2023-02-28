'''Problem 1
Write a program that examines three variables - x, y, and z - and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.'''
x, y, z = int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))
n = 0
if (x > y and x % 2 != 0):
    n = x
elif (x < y and y % 2 != 0):
    n = y
else:
    n = x
if (n < z and z % 2 != 0 and n != 0):
    n = z
if (n == 0):
    print("There is no odd number amongst the provided numbers.")
else:
    print("The largest odd number among the given numbers is: ", n)
