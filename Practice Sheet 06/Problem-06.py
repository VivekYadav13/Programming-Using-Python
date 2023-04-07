'''
An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them. For example, RAM is an acronym for "random access memory." Write a program that allows the user to type in a phrase and then outputs the acronym for that phrase. Note : The acronym should be all uppercase, even if the words in the phrase are not capitalized.
'''

ab = input("Enter an abbreviation: ")
ac = ''
for i in range(len(ab)):
    if i != (len(ab) - 1):
        if i == 0:
            if 97 <= ord(ab[i]) <= 122:
                ac += chr(ord(ab[i])-32)
            else:
                ac += ab[i]
        elif ab[i] == ' ' and ab[i+1] != ' ':
            if 97 <= ord(ab[i+1]) <= 122:
                ac += chr(ord(ab[i+1])-32)
            else:
                ac += ab[i+1]
print("Acronym is:", ac)
