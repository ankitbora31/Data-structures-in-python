"""
a tuple is a sequence of immutable Python objects.
these are sequences just like lists.
"""

tup1 = (1, 2, 3, 4, 5)
tup2 = ('a', 'b', 'c', 'd')
tup3 = ()  # empty tuple
tup4 = (50, )  # a tuple containing single value

# accessing tuples
print(tup1[0])
print(tup2[1:3])

# updating tuples
tup = tup1 + tup2
print(tup)

# deleting or inserting elements in tuple is not possible
# entire tuple can be deleted though
del tup
print(tup)  # it results in error since tup is deleted

"""
basic tuple operations
len() length
and others same as lists
"""