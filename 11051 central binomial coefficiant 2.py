import sys, math

N,K = map(int, sys.stdin.readline().split(' '))
fact = math.factorial
if K < 0 or K >N:
    num = 0
else:
    num = fact(N)//(fact(K)*fact(N-K))
print(num%10007)
 ​