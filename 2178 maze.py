import array as arr
import collections

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))


def Maze():
    q = collections.deque([])
    q.append([0, N - 1, M - 1])
    visited = arr.array('d')
    while q:
        c, x, y = q.pop()

        if (x, y) == (0, 0):
            break
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nc, nx, ny = c + 1, x + dx, y + dy
            if (nx + (ny * 0.001)) in visited:
                continue
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if maze[nx][ny] == 0:
                continue
            q.insert(0, [nc, nx, ny])
            visited.append(nx + (ny * 0.001))

    print(c + 1)


Maze()