from collections import deque
cnt = 1 #need to clean the first location. min cnt ==1

def turn(N,M,d):
    if d == 0:
        M -= 1
    elif d == 1:
        N -= 1
    elif d ==2:
        M += 1
    else:
        N += 1
    return(N,M)

def check_left(N, M, d):
    dfs = deque() #큐생성
    stack = deque(arr(turn(N, M, d))) #다음 체크할 칸
    visit = [] # 방문 내역
    while len(visit) < 4:  #4방향 다 체크 할때까지
        next = stack.popleft() #다음 체크 꺼냄
        if next == 1: #1이라면
            visit.append(d) #d visit에 추가
            d += 1 if d < 3 else d == 0 #왼쪽으로 돌기
        else:   #아니면
            arr[N,M] = 1 #1로 바꾸기 추가
            cnt += 1 #청소한 횟수 1추가
            return dfs #다시 처음부터 체크
        break

while True:
    N,M = map(int, input().split(''))
    r,c,d = map(int, input().split(''))
    arr = [int(input()) for i in range(N)]


    while check_left(N, M, d): #4방향 다 체크했는데 넷 다 1일경우 break
        #Go Back
        d += 1 if d < 3 else d == 0
        turn(N, M, d)
        if arr[N, M] == 1: #후진한 자리가 1일경우
            break
        else:
            continue