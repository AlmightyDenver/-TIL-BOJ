def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while key < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

n = int(input())
ARR = [int(input()) for i in range(n)]
print(insertion_sort(ARR))