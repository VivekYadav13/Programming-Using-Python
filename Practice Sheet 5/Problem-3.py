"""
Write a program that asks the user to enter a string s and then converts s to lowercase, removes
all the periods and commas from s, and prints the resulting string.
"""
def finalstring(string):
    ns = ''
    for ch in string:
        if ord(ch) >= 65 and ord(ch) <= 91:
            ns += chr(ord(ch)+32)
        elif ch not in ['.', ',']:
            ns += ch
    return ns


s = str(input('Enter your string: '))
print('Final string is: ', finalstring(s))
