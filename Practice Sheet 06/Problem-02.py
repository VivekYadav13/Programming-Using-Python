'''
Create a list of random numbers and remove all duplicate elements in the list.
'''

import random
list = [(random.randint(0, 10)) for i in range(10)]
list.sort()
newlist = []
for i in range(10):
    if list[i] != list[i-1]:
        newlist += [i]
print("List with removed duplicates is:", newlist)
