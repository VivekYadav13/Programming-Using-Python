'''

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
