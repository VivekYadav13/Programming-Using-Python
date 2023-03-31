'''
Write a function to calculate the area of a pizza and its cost per square metre, given its radius. Given n sections of pizza, find the cost of each section.
'''

import math


def area(radius):
    return math.pi*radius*radius


def cost(cost, area):
    return cost*area


r = eval(input("Enter radius of the pizza: "))
c = eval(input("Enter cost (/unit^2): "))
n = eval(input("Enter number of sections: "))
print("Area of the given pizza is: ", area(r))
print("Cost of the pizza is: ", cost(c, area(r)))
print("Cost of each section is: ", (cost(c, area(r)))/n)
