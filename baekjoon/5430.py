import sys
from collections import deque

t = int(input())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    q = deque(arr)

    rev, front, back = 0, 0, len(q)-1
    flag = 0
    if n == 0:
        q = []
        front = 0
        back = 0

    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(q) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if flag == 0:
        if rev % 2 == 0:
            print('['+','.join(q) +']')
        else:
            q.reverse()
            print('['+','.join(q) +']')