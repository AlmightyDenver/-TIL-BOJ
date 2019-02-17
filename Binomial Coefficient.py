#1
def BiCoef(n, k):
    if n  == k or k == 0:
        return 1
    elif k == 1:
        return n
    elif k > n:
        return 0
    return fact(n) // (fact(k)*fact(n-k))

print(BiCoef(n, k))

#2
def bicoe(n, k):
    if k > n:
        return 0
    else:
        V = 1
        for i in range(1, min(k, n - k) + 1):
            V = (V * (n - i + 1) // i)
        return V


print(bicoe(n, k))
