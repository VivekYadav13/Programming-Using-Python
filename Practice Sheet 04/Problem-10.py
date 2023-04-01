'''
Write a function that computes the area of a triangle given the length of its three sides as parameters.
'''

def area(x, y, z):
    s = (x+y+z)/2
    A = (s*(s-x)*(s-y)*(s-z))**(1/2)
    return A


a = eval(input("Enter length of first side of the triangle: "))
b = eval(input("Enter length of second side of the triangle: "))
c = eval(input("Enter length of third side of the triangle: "))
print("Area of a triangle with given sides =", area(a, b, c))
