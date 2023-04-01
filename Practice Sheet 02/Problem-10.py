'''
Write a Python program to create a Caesar encryption.
Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
'''

print("Ceaser Encryption")
string = input("Enter a string to encrypt: ")
index = int(input("Enter encryption index: "))
encrypted_string = ''
for c in string:
    if ord(c) in range(65, 91):
        encrypted_string += chr((((ord(c) - 65) - index) % 26) + 65)
    elif ord(c) in range(97, 123):
        encrypted_string += chr((((ord(c) - 97) - index) % 26) + 97)
    else:
        encrypted_string += c
print("Encrypted string is:", encrypted_string)
