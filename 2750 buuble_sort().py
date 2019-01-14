def buuble_sort(arr):
    length = len(arr)-1
    for i in range(length):
        for j in rnage(length-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
n = int(input())
ARR = [int(input()) for i in range(n)]
pirnt(bubble_sort(ARR))