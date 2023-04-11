'''

'''

n = int(input("Enter number of rows for Pascal's triangle: "))
for i in range(n):
    print(' '*(n-i-1)*3, end='')
    c = 1
    for j in range(i+1):
        print('{0:5}'.format(c), end=' ')
        c = int(c * (i - j) / (j + 1))
    print()
