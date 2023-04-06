'''
Write Python code for matrix multiplication
'''

a = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
b = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
d = []
for i in range(len(a)):
    c = []
    for j in range(len(a[0])):
        t = 0
        for k in range(len(b[0])):
            t += a[i][k] * b[k][j]
        c += [t]
    d = d + [tuple(c)]
print(tuple(d))
