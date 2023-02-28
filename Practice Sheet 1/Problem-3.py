'''
Problem 3:
Translate each of the following mathematical expressions into an equivalent Python expression. You may assume that the math library has been imported (via import math).
A) (3+4)(5)
B) (n(n-1))/2
C) 4(pi)r^2
D) sqrt(r((cos a)^2)+r((sin b)^2))
E) (y2-y1)/(x2-x1)
'''

print("Part A: (3+4)(5) = ", (3+4)*(5))

n = eval(input("Enter a number (n) for part B: "))
print("Part B: (n(n-1))/2 = ", (n*(n-1))/2)

p = 3.1415  # Value of Pi
r = eval(input("Enter a radius (r) for part C: "))
print("Part C: 4(pi)r^2 = ", 4*(p)*(r**2))

print("Part D: Multi inputs and math library is not taught yet.")

x1, x2, y1, y2 = eval(input("Enter a value of x1 for part E: ")), eval(input("Enter a value of x2 for part E: ")), eval(input("Enter a value of y1 for part E: ")), eval(input("Enter a value of y2 for part E: "))
print("Part E: (y2-y1)/(x2-x1) = ", (y2-y1)/(x2-x1))
