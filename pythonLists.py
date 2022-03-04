"""
list is a most versatile data type available in python
which can be written as list comma-separated values
between square brackets.
"""
# lists
list1 = ['physics', 'chemistry', 1991, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ['a', 'b', 'c', 'd']

# accessing values in lists
print("list1[0]: ", list1[0])
print('list2[1:5]: ', list2[1:5])

# updating lists
list2[2] = 6
print(list2)

# delete list elements
del list1[2]
print(list1)

"""
basic list operations
len() = length
[1,2,3] + [4,5,6] = [1,2,3,4,5,6] (concatenation)
['he']*4 = ['he','he','he','he'] (repetition)
3 in [1,2,3] = True (membership)
for x in [1,2,3]: print(x)  iteration
"""