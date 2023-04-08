'''
Write a program that counts the number of words in a sentence entered by the user.
'''

s = input("Enter a sentence: ")
n = 1
for i in range(len(s)):
    if s[i] == ' ' and s[i+1] != ' ':
        n += 1
print("There are", n, "words in the sentence.")
