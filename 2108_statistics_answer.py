import sys
import collections
N = int(input())
a = sorted(map(int,sys.stdin))
mean = (sum(a)*2+N)//N//2
median = a[N//2]
c = collections.Counter(a)
m = max(c.values())
modes = sorted(i for i in c if c[i] ==m)
mode = modes[1%len(modes)]
rge = a[-1] - a[0]
print(mean)
print(median)
print(mode)
print(rge)