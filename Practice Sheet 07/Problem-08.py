'''
A palindrome is a phrase (a string) that reads the same forwards and backwards. The name “hannah” is a palindrome; so is “Ogopogo,” the name of a monster who lives in lake Okanogan, and the word “redivider.” Write a Python program that determines whether a given string is a palindrome.
'''

word = input("Enter a word: ")
reverse = ''
for i in range(len(word)-1, -1, -1):
    reverse += word[i]
if word == reverse:
    print("Given word is a palindrome.")
else:
    print("Given word is not a palindrome.")
