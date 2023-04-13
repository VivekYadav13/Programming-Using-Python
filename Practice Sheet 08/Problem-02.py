'''
Create a 5×5 list of random numbers between 1 and 20. Then write a program that creates a dictionary whose keys are the numbers and whose values are the how many times the number occurs. Then print the three most common numbers.
'''

from random import randint
m = []
d = {}
for i in range(5):
    m += [[randint(1, 20) for j in range(5)]]
    for j in range(len(m[i])):
        if d.get(m[i][j]) == None:
            d[m[i][j]] = 1
        else:
            d[m[i][j]] += 1
print(d)
