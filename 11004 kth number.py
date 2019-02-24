import sys

N, k = map(int, sys.stdin.readline().split())
alist = list(map(int,sys.stdin.readline().strip().split(' ')))

alist.sort()
print(alist[k-1])