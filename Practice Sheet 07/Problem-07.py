'''
Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
Original Tuple:
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:
[30.5, 34.25, 27.0, 23.25]
Original Tuple:
((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
Average value of the numbers of the said tuple of tuples:
[25.5, -18.0, 3.75]
'''

original = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
average = []
sum = 0
for i in range(len(original)):
    for j in range(len(original[i])):
        sum += original[j][i]
    average += [sum/len(original)]
    sum = 0
print(average)
