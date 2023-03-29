"""
Fibonacci Numbers. The Fibonacci number sequence is 1, 1, 2, 3, 5, 8, 13, 21, etc. In other words, the next value of the sequence is the sum of the previous two values in the sequence. Write a routine that, given N, displays the value of the Nth Fibonacci number.
For example, the first Fibonacci number is 1, the 6th is 8, and so on. Write a function to calculate nth Fibonacci number.
"""
def fibonacci(n):
    f = 1
    s = 1
    print(f, s, sep=", ", end=", ")
    for i in range(n-2):
        nxt = f + s
        f = s
        s = nxt
        print(nxt, end=", ")


fibonacci(eval(input("Enter number of numbers: ")))
