"""
each key is separated from its value by a colon(:)
the items are separated by commas, and the whole thing is
enclosed in curly braces.
an empty dictionary -- {}
keys are unique while values can be same
"""

dict1 = {'Name': 'Naruto', 'Age': 21, 'Address': 'xyz'}
print(dict1)

# accessing values in dictionary
print(dict1['Name'])
print(dict1['Address'])

# updating dictionary
dict1['Age'] = 23
dict1['Address'] = 'Leaf Village'
print(dict1)

# deleting elements
del dict1['Age']  # removes entry with Age key
print(dict1)
# del dict1  # removes entire dictionary

# keys must be immutable

# insertion of new keys
dict1['class'] = 'btech'  # inserting new key class with value btech
print(dict1)