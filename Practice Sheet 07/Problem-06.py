'''
Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
'''

given = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
final = []
for i in range(len(given)):
    if len(given[i]) != 0:
        final.append(given[i])
print(final)
