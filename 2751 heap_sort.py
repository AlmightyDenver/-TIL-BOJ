#heapify 자식, 부모 비교해서 큰게 부모로
def heapify(arr, idx, h_size):
    largest = idx
    lft_idx = 2 * idx + 1
    rgt_idx = 2 * idx + 2
    if lft_idx < h_size and arr[lft_idx] > num[largest]:
        largest = lft_idx
    if rgt_idx < h_size and arr[rgt_idx] > num[largest]:
        largest = rgt_idx
    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify(arr, largest, h_size)

"""
1. heapify로 최대 힙 구성
2. 최대 힙의 루트노드인 배열의 맨앞, 맨뒤 교환(largest가 맨뒤로)
3. 맨 마지막 원소를 뺀(n-1)새 루트 노드에 최대 힙 구성
4. 반복
"""
def heap_sort(arr):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr


n = int(input())
num = [int(input()) for _ in range(n)]
sorted = heap_sort(num)
for a in range(len(sorted)):
    print(sorted[a])