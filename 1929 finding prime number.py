import math

def isPr(x):
    if x <2:
        return False
    for i in range(2, (int(math.sqrt(x))+1)):
        if x%i==0: return False
    return True

M, N = map(int, input().split())
for n in range(M,N+1):
    if(Pr(n)): print(n)
