'''
Write a program that uses a dictionary that contains ten usernames and passwords. The program should ask the user to enter their username and password. If the username is not in the dictionary, the program should indicate that the person is not a valid user of the system. If the username is in the dictionary, but the user does not enter the right password, the program should say that the password is invalid. If the password is correct, then the program should tell the user that they are now logged in to the system.
'''

set = {'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3', 'user4': 'pass4', 'user5': 'pass5',
       'user6': 'pass6', 'user7': 'pass7', 'user8': 'pass8', 'user9': 'pass9', 'user10': 'pass10'}
username = input("Enter username: ")
password = input("Enter password: ")
if username not in list(set.keys()):
    print("Access denied! Person is not a valid user!")
elif password != set[username]:
    print("Access denied! Invalid password!")
else:
    print("Access granted!")
