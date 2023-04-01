'''
Write a program to calculate the area of a triangle given the length of its three sides - a, b, and c - using these formulas:
s = (a+b+c)/2
A = sqrt(s(s-a)(s-b)(s-c))
'''

print("Calculating area of a triangle with given lengths of sides.")
a = eval(input("Enter length of first side (a): "))
b = eval(input("Enter length of second side (b): "))
c = eval(input("Enter length of third side (c): "))
s = (a+b+c)/2
A = (s*(s-a)*(s-b)*(s-c))**(1/2)
print("Calculating area using Heron's formula, \nSemi-perimeter of the triangle is: \ns = (a+b+c)/2 =", s, "units", "\nThus, area A of the triangle with given sides is: \nA = sqrt(s(s-a)(s-b)(s-c)) =", A, "units", sep=" ")
