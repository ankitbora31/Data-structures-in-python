"""
heap is a special tree structure in which each parent node
is less than or equal to its child node. then its called
min heap. if each parent node is greater or equal to its
child node its called max heap.
"""
# heapq library is used (inbuilt)
"""functions 
- heapify = converts regular list to a heap 
            (smallest elements get pushed to 0 index)
- heappush = adds new element
- heappop = returns smallest data element
- heapreplace = replaces smallest data element with new element
"""

import heapq

H = [122, 2, 4123, 41, 1230, 123]
heapq.heapify(H)
print(H)

# inserting into heap
heapq.heappush(H, 99)
print(H)

# removing from heap
heapq.heappop(H)
print(H)

# replacing in heap
heapq.heapreplace(H, 6)
print(H)