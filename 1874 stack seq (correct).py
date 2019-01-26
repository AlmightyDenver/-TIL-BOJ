n = int(input())
seq = [int(input()) for _ in range(n)]

stk = []
result = []
k = 0

for i in seq:
    if i >= k:
        while i > k:
            k += 1
            stk.append(k)
            result.append('+')
    if i == stk[-1]:
        stk.pop()
        result.append('-')

if len(stk) != 0:
    print('NO')
else:
    for x in result:
        print(x)