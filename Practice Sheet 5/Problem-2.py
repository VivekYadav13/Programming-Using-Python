"""
Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.
"""
string = input("Enter a string: ")
for ch in string:
    if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print("Given string contains one or more vowels.")
        break
else:
    print("Given string doesn\'t contain any vowel.")
