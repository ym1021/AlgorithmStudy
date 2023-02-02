import sys
sys.stdin = open('../../files/input.txt', 'r')

from collections import deque

M, N, K = map(int, input().split())
data = [[1]*(N+2) for _ in range(M+2)]

for i in range(N+2):
    data[0][i] = 0
    data[M+1][i] = 0
for i in range(1, M+2):
    data[i][0] = 0
    data[i][N+1] = 0

for i in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for j in range(sy+1, ey+1):
        for k in range(sx+1, ex+1):
            data[j][k] = 0

'''
for i in data:
    for j in i:
        print(j, end=' ')
    print()
'''
stk = deque()
_list = []
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
for i in range(1, M+2):
    for j in range(1, N+2):
        resultCnt = 0
        if data[i][j]:
            stk.append(i)
            stk.append(j)
            data[i][j] = 0
            while stk:
                resultCnt += 1
                ux = stk.pop()
                uy = stk.pop()
                for k in range(4):
                    ny = uy + dy[k]
                    nx = ux + dx[k]
                    if data[ny][nx]:
                        stk.append(ny)
                        stk.append(nx)
                        data[ny][nx] = 0
            _list.append(resultCnt)
_list.sort()
'''
for i in data:
    for j in i:
        print(j, end=' ')
    print()
'''
print(len(_list))
print(' '.join(map(str, _list)))
'''
for i in _list:
    print(i, end=' ')
print()'''