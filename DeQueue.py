"""
deque = double ended queue
insertion and deletion can be dealt from both ends
"""

import collections

doubleEnd = collections.deque(['mon','tue','wed'])
print('deque is {}'.format(doubleEnd))

doubleEnd.append('thu')
print('appended at right-{}'.format(doubleEnd))

doubleEnd.appendleft('sun')
print('appended at left-{}'.format(doubleEnd))

doubleEnd.pop()
print('deleting from right-{}',format(doubleEnd))

doubleEnd.popleft()
print('deleting from left-{}'.format(doubleEnd))