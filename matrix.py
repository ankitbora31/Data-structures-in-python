"""
matrix is a special of two dimensional array where each
data element is of strictly same size.
every matrix is 2d array but not vice versa.
"""

# we use numpy package for matrix data manipulation
from numpy import *

a = array([['mon', 18, 20, 22, 17],
           ['tue', 11, 18, 21, 18],
           ['wed', 15, 21, 20, 19],
           ['thu', 11, 20, 22, 21],
           ['fri', 18, 17, 23, 22],
           ['sat', 12, 20, 22, 18],
           ['sun', 14, 16, 15, 19]])

print(a)

print('------------------------------')

# reshaping data
n = a.reshape(5, 7)
print(n)

print('------------------------------')

# accessing values in a matrix
print(a[2])
print(a[3][4])

print('------------------------------')

# adding new row in matrix
a_r = append(a, [['new', 12, 15, 11, 21]], 0)
print(a_r)

print('------------------------------')

# adding a column
a_c = insert(a, [5], [[1], [2], [3],
                      [4], [5], [6], [7]], 1)
print(a_c)

print('------------------------------')

# deleting a row
a = delete(a, [2], 0)
print(a)

print('------------------------------')

# deleting a column
a = delete(a, [2], 1)
print(a)

print('------------------------------')

# update a row in matrix
a[2] = ['updated', 0, 0, 0]
print(a)

"""
in insertion or deletion we have to specify index 0 for
row and 1 for column
"""
