'''
Write a Python script that calculates the roots of a quadratic equation:
ax^2 + bx + c = 0, input values of a, b, c and print the roots.
'''

from math import sqrt
print("Enter values as per ax^2 + bx + c = 0")
a, b, c = eval(input("a = ")), eval(input("b = ")), eval(input("c = "))
discrim = (b**2)-(4*a*c)
if discrim >= 0:
    alpha = (-b+(sqrt(discrim)))/(2*a)
    beta = (-b-(sqrt(discrim)))/(2*a)
    print("Roots of the given quadratic equation are", alpha, "and", beta)
else:
    print("The quadratic equation has imaginary roots.")
