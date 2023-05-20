import sys
from collections import deque
input_ = sys.stdin.readline

n = int(input())
que = deque([])
for _ in range(n):
    cmd = input_().rstrip().split()
    if cmd[0] == 'push':
        que.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(que):
            print(que.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if len(que):
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if len(que):
            print(que[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(que):
            print(que[-1])
        else:
            print(-1)