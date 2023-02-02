import sys
sys.stdin = open('../../files/input.txt', 'r')
#in chk
from collections import deque
def bfs(start):
    visited = [1] * (V + 1)
    q = deque()
    q.append(start)
    visited[start] = 0
    print('bfs : [', end='')
    while q:
        n = q.popleft()
        print(n, end=' ')
        for i in range(1, V + 1):
            if g[n][i] and visited[i]:
                q.append(i)
                visited[i] = 0
    print(']')

V, E = map(int, input().split())
g = [[0]*(V+1) for _ in range(V+1)]
visitedMain = [1]*(V+1)
for i in range(E):
    sn, en = map(int, input().split())
    g[sn][en] = 1
    g[en][sn] = 1
'''
for i in g:
    for j in i:
        print(j, end=' ')
    print()
'''

bfs(1)
