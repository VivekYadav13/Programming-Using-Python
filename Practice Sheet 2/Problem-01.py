'''
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : ‘google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
'''

string = input("Enter a string: ")
uniquechar = []
for ch in string:
    if ch not in uniquechar:
        uniquechar += [ch]
for ch in uniquechar:
    frequency = 0
    for c in string:
        if c == ch:
            frequency += 1
    print(ch, ':', frequency)
