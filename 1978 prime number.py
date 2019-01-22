n = int(input())
num = [int(x) for x in input().split()]
cnt = 0
for i in range(n):
    a = num[i]
    if a == 2 or a == 3:
        cnt += 1
        continue
    elif a == 1 or a% 2 == 0:
        continue
    else:
        k = 3
        while a%k != 0:
            k += 2
            if a <= k:
                cnt += 1
                break
