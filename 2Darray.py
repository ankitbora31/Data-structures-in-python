"""
two dimensional array is an array within an array
it represents tables containing rows and columns
"""

t = [[21, 23, 3, 4], [51, 6, 7, 8], [11, 2, 34, 9]]
print(t)
print('---------------------------')

# accessing elements of 2d array
print(t[0])
print(t[1])
print(t[1][2])
print('---------------------------')

# to print entire 2d array
for r in t:
    for c in r:
        print(c,end=" ")
    print()

print('---------------------------')

# inserting values in 2d array
t.insert(2, [11, 9])
for r in t:
    for c in r:
        print(c, end=" ")
    print()

print('---------------------------')

# updating values in 2d array
t[0][2] = 9
t[1][2] = 111
for r in t:
    for c in r:
        print(c, end=" ")
    print()

print('---------------------------')

# deleting values
del t[2]  # deleting array indexed at 3
del t[0][1]  # deleting 1 index element in 0th array
for r in t:
    for c in r:
        print(c, end=" ")
    print()
