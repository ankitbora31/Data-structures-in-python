"""
a set is a collection of items not in any particular
order, python set id similar to mathematical set.
elements can not be duplicates
elements are immutable while whole set is mutable
set do not support indexing
"""

# creating a set
days = {21, 21, 22}  # using curly braces
print(days)  # here duplicate values are not shown
days = set(['Mon', 'Tue', 'Wed', 'Thur'])  # or using set function
print(days)

print('---------------------------')

# accessing values in set
for d in days:
    print(d)

print('---------------------------')

# adding items to set
days.add('Fri')
print(days)

print('---------------------------')

# removing items from set
days.discard('Thur')
print(days)

print('---------------------------')

# union of sets
daysA = {'mon', 'tue', 'wed', 'fri'}
daysB = {'mon', 'thu', 'fri', 'sat'}
UnionDays = daysA | daysB
print(UnionDays)

print('---------------------------')

# intersection of sets
daysA = {1, 2, 3, 4, 5}
daysB = {2, 3, 6, 7, 8, 9}
IntersectDays = daysA & daysB
print(IntersectDays)

print('---------------------------')

# difference of sets
diffDays = daysA - daysB
print(diffDays)

print('---------------------------')

# compare sets
daysA = set([1, 2, 3, 4, 5])
daysB = set([2, 3, 4, 56, 77, 12, 9])
compareDays = (daysA <= daysB)
print(compareDays)