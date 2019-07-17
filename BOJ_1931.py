# 그리디 : 1931 회의실 배정

import sys

def solve(alist):
    t = 0
    cnt = 0
    for a, b in alist:
        if b >= t:
            cnt += 1
            t = a
    return cnt

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    time = []
    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        time.append([end, start])
    time.sort()
    print(solve(time))