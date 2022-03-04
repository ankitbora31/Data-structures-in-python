"""
Array is a container which can hold a fix number of
items and these should be of the same type.
each item stored in array is called element
location used to identify element is called index
OPERATIONS IN ARRAYS
    traverse
    deletion
    insertion
    search
    update
"""

from array import *
# arrayName = array(type code, [Initializers])
"""
Type codes::
b(signed int of 1B),B(unsigned int of 1B),
i(signed int of 2B),I(unsigned int of 2B),
f(float of 4B),d(floating point of 8B),
c(char of 1B)
"""
array1 = array('i', [10, 20, 30, 40, 50])
for x in array1:
    print(x)  # prints the array

print(array1[0])  # prints element at 0 index

array1.insert(1, 60)  # inserts element 60 at 1 index

array1.remove(40)  # removes element 40

print(array1.index(60))  # prints the index of 40

array1[2] = 80  # updates the element at index 2 to 80

for i in array1:
    print(i)

