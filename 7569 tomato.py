import collections
M,N,H = map(int, input().split())
tmt = []

for _ in range(H):
    lay = []
    for i in range(N):
        lay.append(list(map(int, input().split())))
    tmt.append(lay)

def any_0():
    result = True
    for h in tmt:
        for line in h:
            if 0 in line:
                return (result)
            else:
                result = False
    if not result:
        print(0)


def TOMAT():
    q = collections.deque([])
    mu = [[[False] * M for _ in range(N)] for _ in range(H)]
    for h in range(H):
        for j in range(M):
            for i in range(N):
                if tmt[h][i][j] == 1:
                    q.append([0, h, i, j])
                    mu[h][i][j] = True
                if tmt[h][i][j] == -1:
                    mu[h][i][j] = True

    while q:
        d, h, x, y = q.popleft()
        for dx, dy, dh in (-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1):
            nd, nx, ny, nh = d + 1, x + dx, y + dy, h + dh
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nh < 0 or nh >= H:
                continue
            if mu[nh][nx][ny]:
                continue
            mu[nh][nx][ny] = True
            q.append([nd, nh, nx, ny])

    res = True
    for h in mu:
        for line in h:
            if not all(line):
                res = False
                break
    if res:
        print(d)
    else:
        print(-1)


if any_0():
    TOMAT()