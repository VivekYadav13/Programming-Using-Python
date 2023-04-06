'''
Write a Python function that takes two lists and returns True if they have at least one common member.
'''

def hascommon(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                return True
    return False


list1 = [1, 2, 5, 6, 8]
list2 = [3, 4, 2, 8, 0]
print(hascommon(list1, list2))
