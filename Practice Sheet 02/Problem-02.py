'''

'''

from random import randint


def greedy(n):
    change = {50: randint(0, 20), 25: randint(
        0, 20), 5: randint(0, 20), 1: randint(0, 20)}
    print("Available amount of change is (denomination: number): " + change)
    t = 0
    ch = list(change.keys())
    c = []
    for i in ch:
        t += i * change[i]
    for i in ch:
        q = int(n/i)
        if q > change[i]:
            q = change[i]
        n = n - (q*i)
        c += [q]
    if n > t:
        return "Not enough change, most you can get is (denomination: number): " + c
    else: 
        return "Change is (denomination: number): " + c

n = int(input("Enter amount: "))
print(greedy(n))
