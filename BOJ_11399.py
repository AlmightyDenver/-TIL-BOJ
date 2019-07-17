#11399 Greedy ATM
import sys

def solve(alist):
    alist.sort()
    sum = 0
    for i in range(len(alist)):
        sum += (alist[i] * (len(alist)-i))
    return sum

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    time = list(map(int, sys.stdin.readline().strip().split(' ')))
    print(solve(time))