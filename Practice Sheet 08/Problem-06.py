'''
Python program to sort a dictionary based on its values.
'''

a = {'c': 6, 'e': 7, 'g': 1, 'j': 2, 'k': 2,
     'm': 3, 'q': 6, 's': 9, 'u': 8, 'y': 0}
b = list(a.values())
b.sort()
c = {}
for j in b:
    for i in a:
        if j == a[i] and c.get(i) == None:
            c[i] = j
print("Sorted dictionary based on values is:", c)
