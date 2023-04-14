'''
Determine the maximum and minimum frequency character in a given string. (If multiple characters have maximum and minimum frequency print them all)
'''

s = input("Enter a string: ")
d = {}
h = 0
hl = []
l = float('inf')
ll = []
for c in s:
    if d.get(c) != None:
        d[c] += 1
    elif d.get(c) == None:
        d[c] = 1
for k in d:
    if d[k] > h:
        h, hl = d[k], [k]
    elif d[k] == h:
        hl += [k]
    if d[k] < l:
        l, ll = d[k], [k]
    elif d[k] == l:
        ll += [k]
if len(hl) > 1:
    print(
        f"The characters that repeated highest number of times are {hl} which repeated {h} times.")
elif len(hl) == 1:
    print(
        f"The character that repeated highest number of times is \"{hl[0]}\" which repeated {h} times.")
if len(ll) > 1:
    print(
        f"The characters that repeated lowest number of times are {ll} which repeated {l} times.")
elif len(ll) == 1:
    print(
        f"The character that repeated lowest number of times is \"{ll[0]}\" which repeated {l} times.")
