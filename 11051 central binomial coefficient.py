import sys

N, K = map(int, sys.stdin.readline().split(' '))


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


if K < 0 or K > N:
    num = 0
else:
    num = fact(N) // (fact(K) * fact(N - K))

print(num % 10007)

