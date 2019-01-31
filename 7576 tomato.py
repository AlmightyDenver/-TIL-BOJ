import collections

M, N = map(int, input().split())
tmt = []
for _ in range(N):
    tmt.append(list(map(int, input().split())))

# check any 0 in tmt
result = True
for x in tmt:
    if 0 in x:
        break
    else:
        result = False
if not result:
    print(0)

def TOMAT():
    q = collections.deque([])
    mu = [[False] * M for _ in range(N)]
    for j in range(M):
        for i in range(N):
            if tmt[i][j] == 1:
                q.append([0, i, j])
                mu[i][j] = True
            if tmt[i][j] == -1:
                mu[i][j] = True

    while q:
        d, x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nd, nx, ny = d + 1, x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mu[nx][ny]:
                continue
            mu[nx][ny] = True
            q.append([nd, nx, ny])
    res = True
    for x in mu:
        if not all(x):
            res = False
            break
    if res:
        print(d)
    else:
        print(-1)

if result:
    TOMAT()