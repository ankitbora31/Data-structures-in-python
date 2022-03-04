"""
Hash table
it is a type of data structure in which the address or the
index value of the data element is generated from a hash
function.that makes accessing the data faster as the index
value behaves as a key for the data value.
hash table stores key-value pairs but the key is
generated through a hashing function.

in python, the dictionary data types represent the
implementation of hash tables
"""

# # accessing values in dictionary
# dict = {'name': 'ankit', 'age': 20, 'class': 'btech'}
# print(dict)
# print("dict['name']: ", dict['name'])
# print('dict["class"]: ', dict['class'])
#
# # updating dictionary
# dict['age'] = 21
# print(dict)
#
# # deleting dictionary elements
# del dict['age']
# print(dict)

# a = map(hash, [0, 1, 2, 3])
# print(hash(a))
# b = map(hash, ['0', '1', '2', '3'])
# print(hash('0'))

import pprint
class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for _ in range(self.bucket_size)]
        self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key, value))

    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return value
        return None

    def __str__(self):
        return pprint.pformat(self.buckets)

if __name__ == '__main__':
    capitals = [
        ('France', 'Paris'),
        ('United States', 'Washington D.C.'),
        ('Italy', 'Rome'),
        ('Canada', 'Ottawa')
    ]

hashtable = Hashtable(capitals)
print(hashtable)
a = hashtable.get_value('Canada')
print(a)