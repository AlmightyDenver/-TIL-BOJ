import sys
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, num):
        self.stack.append(num)
    def pop(self):
        print(self.stack.pop() if self.stack else -1)
    def size(self):
        print(len(self.stack))
    def empty(self):
        print(0 if self.stack else 1)
    def top(self):
        print(self.stack[-1] if self.stack else -1)

stack = Stack()
for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip()
    if cmd[:4] == 'push':
        stack.push(int(cmd[5:]))
    elif cmd == 'pop':
        stack.pop()
    elif cmd == 'size':
        stack.size()
    elif cmd == 'empty':
        stack.empty()
    elif cmd == 'top':
        stack.top()
