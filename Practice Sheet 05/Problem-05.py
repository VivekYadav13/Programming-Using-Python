'''
Write a function called closest that takes a list of numbers L and a number n and returns the largest element in L that is not larger than n. For instance, if L=[1,6,3,9,11] and n=8, then the function should return 6, because 6 is the closest thing in L to 8 that is not larger than 8. Return “No Match” if all of the things in L are greater than n.
'''

def closest(L, n):
    a = 0
    for i in range(len(L)):
        if a <= L[i] <= n:
            a = L[i]
    if a == 0:
        return "No Match"
    else:
        return a


l = int(input("Enter length of list: "))
L = []
for i in range(l):
    L += [eval(input("Enter number " + str(i+1) + ": "))]
n = eval(input("Enter number to check: "))
print("Largest number in", L, "not larger than", n, "is", closest(L, n))
