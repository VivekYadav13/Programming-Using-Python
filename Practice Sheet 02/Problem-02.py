'''
The numerical values of coins have been arranged so that the greedy algorithm will result in the smallest number of coins when making change. This means that the largest valued coin is tried first, and as many of those coins are used as possible. Then the next smaller denomination coin is used, and so on until the pennies are dealt out. So for 84 cents in change, a 50-cent piece could be used (leaving 34 cents), then a 25- cent piece (leaving 9 cents), a 5 cent piece (leaving 4 cents), and 4 pennies. If no 50- cent piece was available, then 25-cent pieces would be used in its place: 3 quarters, followed by a nickel and four pennies. Write a program that reads a number between 1 and 99 that is an amount of change to be given and prints the coin values that would be used.
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
