#HEAP

from heapq import *
heap = []
data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
for item in data:
    heappush(heap, item)
#heap : [(1, 'J'), (2, 'O'), (3, 'H'), (4, 'N')]. sorted
while heap:
    print(heappop(heap)[1])
    """J
    O
    H
    N

    the first is 1 not 0
"""

from heapq import heappush, heappop
heap = []
data = [1,0,2,9,3,4,7]
for item in data:
    heappush(heap, item)
print(heap) #[0, 1, 2, 9, 3, 4, 7]
print(heap == data) # False
ordered = []
while heap:
    ordered.append(heappop(heap))

print(ordered)
data.sort()
print(data == ordered)


import heapq
H = [21,1,4,8]
heapq.heapify(H)
print(H) #[1, 8, 4, 21]
heapq.heappush(H,8)
print(H) #[1, 8, 4, 21, 8]
heapq.heapreplace(H, 6)
print(H) #[4, 8, 6, 21, 8]