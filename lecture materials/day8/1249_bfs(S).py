import sys
sys.stdin = open('../../files/input.txt', 'r')
from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]

INF = 987654321
tc = int(input())+1
for testCase in range(1, tc):
    N = int(input())
    g = [[0]*(N+2)]
    for i in range(1, N+1):
        g.append([0])
        g[i].extend(list(map(int, input())))
        g[i].append(0)
    g.append([0]*(N+2))

    dist = [[0] * (N + 2)]
    for i in range(1, N + 1):
        dist.append([0])
        dist[i].extend([INF]*N)
        dist[i].append(0)
    dist.append([0] * (N + 2))
    q = deque()

    dist[1][1] = 0
    q.append((1,1))
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if dist[ny][nx] > dist[cy][cx]+g[ny][nx]:
                dist[ny][nx] = dist[cy][cx] + g[ny][nx]
                q.append((ny, nx))
    print('#%d %d' %(testCase, dist[N][N]))

