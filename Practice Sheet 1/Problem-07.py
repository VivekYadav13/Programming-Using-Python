'''
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 4 and how many end in a 9.
'''

squarecount4 = 0
squarecount9 = 0
for i in range(1, 101):
    if str(i**2)[-1] == '4':
        squarecount4 += 1
    elif str(i**2)[-1] == '9':
        squarecount9 += 1
print("Number of squares between 1 to 100 that end with 4 are",
      squarecount4, "and that end with 9 are", squarecount9)
