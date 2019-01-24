n = int(input())
seq = [int(input()) for _ in range(n)]
stk = []
result = []
k = 0
try:
    for i in range(1, seq[0]+1):
        k+=1
        stk.append(k)
        result.append('+')

    for j in range(n):
        if seq[j] > stk[-1]:
            while stk[-1] < seq[j]:
                k+=1
                stk.append(k)
                result.append('+')
        if seq [j] <= stk[-1]:
            stk.pop()
            result.append('-')

    for x in range(len(result)):
        print(result[x])

except:
    print("NO")