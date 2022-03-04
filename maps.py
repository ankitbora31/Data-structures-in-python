"""
python maps also called chainMap is a type of data structure
to manage multiple dictionaries together as one unit.
we use chainMap method from collections library
"""

import collections

dict1 = {'sem1': 1, 'sem2': 2}
dict2 = {'sem3': 3, 'sem4': 4}

res = collections.ChainMap(dict1, dict2)

print(res)
print(res.maps)

print('---------------------------')

# to print keys
print('keys= {}'.format(list(res.keys())))

# to print values
print('values= {}'.format(list(res.values())))

print('---------------------------')

# to print all elements from the result
for key, val in res.items():
    print('{} = {}'.format(key,val))
print()

print('---------------------------')

# to find a specific value present or not in the result
print('sem3 in res: {}'.format(('sem3' in res)))
print('sem5 in res: {}'.format(('sem5' in res)))


"""Map recording - if we change the order of the
dictionaries while clubbing them we see position of 
elements gets interchanged. this shows the behaviour 
of maps as stacks.
"""
print('---------------------------')

# updating map
dict2['sem3'] = 5
print(res.maps)

"""
performing insertions and deletions in dictionaries 
are done dictionaries program
"""