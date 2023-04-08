'''
One way to calculate the square root of a number is to use Newton’s method. This starts with an initial guess: if the square root of x is being computed, then a fair initial guess g would be x/2. Successive estimates are given by the expression: newg = (g + x/g)/2 Successive estimates are nearer and nearer to the actual square root. Write a program to compute the square root of a number that is entered from the keyboard.
'''

x = eval(input("Enter a number: "))
g = x/2
for i in range(10):
    g = (g+(x/g))/2
print("Square root of given number using Newton's method is:", g)
