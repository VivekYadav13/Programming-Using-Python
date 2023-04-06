'''
Write a Python program to find the list of words that are longer than n from a given list of words.
'''

l = int(input("Enter length of the list: "))
list = []
for i in range(l):
    list += [(input("Enter word: "))]
n = int(input("Enter a word length: "))
newlist = []
for i in range(len(list)):
    if len(list[i]) >= n:
        newlist += [list[i]]
print("The list with words with length more than equal to", n, "is", newlist)
