'''
Determine the kth non repeating character in a string.
'''

s = input("Enter a string: ")
k = int(input("Enter which letter to check: "))
u = []
d = []
for ch in s:
    if ch not in u and ch not in d:
        u.append(ch)
    elif ch in u:
        u.remove(ch)
        d.append(ch)
if k > len(u):
    print('The ', k, 'th non repeating character doesn\'t exist.', sep='')
else:
    print('The ', k, 'th non repeating character is ', u[k-1], sep='')
