'''
Extract unique values from a random dictionary.
'''

d = {1: 'a', 5: 'b', 7: 'b', 3: 'c', 8: 'b', 2: 'd', 0: 'a', 9: 'b', 4: 'c', }
l = list(d.values())
t = dict.fromkeys(l)
print('Unique values are', tuple(t.keys()))
