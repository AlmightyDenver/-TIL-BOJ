"""
import sys
nums = map(int, sys.stdin.readlines()[1:])
print('\n'.join(map(str,sorted.nums)))



import sys, heapq
I = sys.stdin.readline
P = sys.stdout.write

N = int(I())
A = []
heapq.heapify(A)
for _ in range(N):
    heapq.heappush(A, int(I()))
print('\n'.join(map(str, heapq.nsmallest(N, A))))
print('\n'.join(map(str, heapq.nlargest(N,A))))



import sys


def MergeSort(A):
    if len(A) < 2: return
    m = len(A) >> 1
    L = A[:m];
    MergeSort(L)
    R = A[m:];
    MergeSort(R)

    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[i + j] = L[i]
            i += 1
        else:
            A[i + j] = R[j]
            j += 1
    A[i + j:] = L[i:] or R[j:]


A = list(map(int, sys.stdin.readlines()));
A.pop(0)
MergeSort(A)
sys.stdout.write('\n'.join(map(str, A)))
"""

import sys, heapq
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readlines()))
sys.stdout.write('\n'.join(map(str, heapq.nsmallest(n, data))))