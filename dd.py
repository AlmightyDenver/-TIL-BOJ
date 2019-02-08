import sys

N = 5
A = [2,4,8,0,3]

MAX_NUM = 10001
count = [0] * (MAX_NUM)
countSum = [0] * (MAX_NUM)

for i in range(0, N):
    count[A[i]] += 1

countSum[0] = count[0]

for i in range(1, MAX_NUM):
    countSum[i] = countSum[i - 1] + count[i]

B = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    B[countSum[A[i]]] = A[i]
    countSum[A[i]] -= 1

for i in range(1, len(B)):
    print(B[i])