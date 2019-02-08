import sys, heapq
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readlines()))
sys.stdout.write('\n'.join(map(str, heapq.nsmallest(n, data))))