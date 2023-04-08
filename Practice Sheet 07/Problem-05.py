'''
Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
'''

given = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
list = list((given[i][1], given[i][0]) for i in range(len(given)))
list.sort(reverse=True)
sortedgiven = tuple((list[i][1], list[i][0]) for i in range(len(list)))
print(sortedgiven)
