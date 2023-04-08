'''
Write a program that finds the average of a series of numbers entered by the user (random numbers). As in the previous problem, the program will first ask the user how many numbers there are. Note: The average should always be a float, even if the user inputs are all ints.
'''

n = int(input("How many numbers are there? - "))
a = 0
for i in range(n):
    a += eval(input("Enter number " + str(i+1) + ": "))
print("The average of given numbers is", a/n)
