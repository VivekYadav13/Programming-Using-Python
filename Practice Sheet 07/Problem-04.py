'''
Sort a tuple using second element tuple1 = (('b', 37),('c', 11),('d',29),('a', 23))
'''

tuple1 = (('b', 37), ('c', 11), ('d', 29), ('a', 23))
list1 = list((tuple1[i][1], tuple1[i][0]) for i in range(len(tuple1)))
list1.sort()
sortedtuple1 = tuple((list1[i][1], list1[i][0]) for i in range(len(list1)))
print(sortedtuple1)
