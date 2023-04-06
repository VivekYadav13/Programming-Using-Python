'''
Sort a tuple using first element tuple1 = (('b', 37),('c', 11), ('d',29),('a', 23))
'''

tuple1 = (('b', 37), ('c', 11), ('d', 29), ('a', 23))
list1 = list(tuple1)
list1.sort()
sortedtuple1 = tuple(list1)
print(sortedtuple1)
