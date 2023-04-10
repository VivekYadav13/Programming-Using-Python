'''

'''

n = int(input("Enter number of rows for Pascal's triangle: "))
for i in range(n):
    print(' '*(n-i-1), end='')
    c = 1
    for j in range(i+1):
        print(c, end=' ')
        c = int(c * (i - j) / (j + 1))
    print()
