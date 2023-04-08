'''
Write a Python program to find the list of words that are longer than n from a given list of words.
'''

l = int(input("Enter length of list: "))
L = []
for i in range(l):
    L += [input("Enter word " + str(i+1) + ": ")]
n = eval(input("Enter number of letters to check: "))
a = []
for i in range(len(L)):
    if len(L[i]) >= n:
        a += [L[i]]
print("Words in", L, "larger than", n, "are/is", a)
