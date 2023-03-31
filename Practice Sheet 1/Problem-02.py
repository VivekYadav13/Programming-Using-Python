'''
Write a program that asks user to enter 10 integers, and then prints the largest odd number that was entered. If no odd number was entered, it should print a message to that effect.
'''

numberarray = []
for i in range(10):
    number = int(input("Enter number " + str(i+1) + ": "))
    numberarray += [number]
oddnumberarray = []
for n in numberarray:
    if n % 2 != 0:
        oddnumberarray += [n]
if oddnumberarray == []:
    print("No odd numbers were entered")
elif oddnumberarray != []:
    odd = 0
    for n in oddnumberarray:
        if n > odd:
            odd = n
    print("Largest odd number amkngst the entered numbers is ", odd)
