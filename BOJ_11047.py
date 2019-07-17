import sys

def Coin(coin_list, K):
    cnt = 0
    for i in range(N-1, -1, -1):
        cnt += (K // coin_list[i])
        K %= coin_list[i]
    return cnt

if __name__ == "__main__":
    #N, K = 10, 4200
    #coin_list = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
    N, K = list(map(int, sys.stdin.readline().strip().split()))
    coin_list = [int(sys.stdin.readline().strip()) for i in range(N)]
    print(Coin(coin_list, K))


# 시간 초과
# def Coin(coin_list, K):
#     cnt = 0
#     for i in coin_list:
#         while K >= i:
#             K -= i
#             cnt += 1
#     return cnt
