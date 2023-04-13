'''
Python program to find the sum of all items in a dictionary.
'''

a = {'q': 3, 'z': 9, 'c': 5, 'p': 7, 'f': 2,
     'y': 8, 'b': 6, 'x': 1, 'd': 4, 'h': 0}
sum = 0
for i in list(a.values()):
    sum += i
print("Sum of all items in the dictionary is:", sum)
