'''
Write a function that returns the value of a quadratic function at a particular x value. A quadratic is a polynomial of the form: ax2 + bx + c
The function quad() is passed values for a, b, c, and x and returns the value of the polynomial.
'''

def quad(a, b, c, x):
    return (a*x*x)+(b*x)+c


print("For the quadratic polynomial ax^2 + bx + c,")
a, b, c, x = eval(input("Enter value of a: ")), eval(input("Enter value of b: ")), eval(input("Enter value of c: ")), eval(input("Enter value of x: "))
print("The value of polynomial ", a, "x^2 + ", b, "x + ", c, " at x=", x, " is ", quad(a, b, c, x), sep='')
