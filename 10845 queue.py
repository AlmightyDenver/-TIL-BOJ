import sys

class Q:
    def __init__(self):
        self.q = []
    def push(self, x):
        self.q.append(x)
    def pop(self):
        if self.q:
            print(self.q[0])
            del self.q[0]
        else:
            print(-1)
    def size(self):
        print(len(self.q))
    def empty(self):
        if self.q:
            print(0)
        else:
            print(1)
    def front(self):
        if self.q:
            print(self.q[0])
        else:
            print(-1)
    def back(self):
        if self.q:
            print(self.q[-1])
        else:
            print(-1)

que = Q()
for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip()
    if cmd[:4] == 'push':
        que.push(int(cmd[5:]))
    elif cmd == 'pop':
        que.pop()
    elif cmd == 'size':
        que.size()
    elif cmd == 'empty':
        que.empty()
    elif cmd == 'front':
        que.front()
    elif cmd == 'back':
        que.back()