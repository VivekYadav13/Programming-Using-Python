'''
Python program to sort a dictionary based on its keys.
'''

a = {7: 'c', 6: 'f', 0: 'j', 8: 'm', 9: 'p',
     5: 's', 4: 'u', 2: 'w', 1: 'y', 3: 'z'}
b = list(a.keys())
b.sort()
c = {}
for i in b:
    c[i] = a[i]
print("Sorted dictionary based on keys is:", c)
