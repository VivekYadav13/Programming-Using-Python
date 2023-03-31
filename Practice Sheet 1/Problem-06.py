'''
Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them whether they got it right or wrong and what the correct answer is.
'''

from random import randint
for i in range(10):
    a = randint(0, 9)
    b = randint(0, 9)
    ans = int(input("Question " + str(i+1) + ": " +
                    str(a) + " x " + str(b) + " = "))
    if ans == a*b:
        print("Right!")
    else:
        print("Wrong!")
