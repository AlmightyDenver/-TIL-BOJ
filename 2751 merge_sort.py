n = int(input())
num = [int(input()) for _ in range(n)]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        l = merge_sort(left)
        r = merge_sort(right)
        return merge(l,r)
def merge(l,r):
    i = 0
    j = 0
    sorted = []
    while (i < len(l)) and (j < len(r)):
        if l[i] < r[j]:
            sorted.append(l[i])
            i +=1
        else:
            sorted.append(r[j])
            j+=1
    while i < len(l):
        sorted.append(l[i])
        i += 1
    while j < len(r):
        sorted.append(r[j])
        j+=1
    return sorted

sorted = merge_sort(num)
for a in range(len(sorted)):
    print(sorted[a])