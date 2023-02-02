import sys
sys.stdin = open('../../files/input.txt', 'r')

import heapq

T = int(input()) + 1

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
INF = 987654321
for test_case in range(1, T):
    N = int(input())
    dist = [[INF] * N for _ in range(N)]
    g = [list(map(int, input())) for _ in range(N)]

    dist[0][0] = 0
    pq = []
    heapq.heappush(pq, (0, 0, 0))

    while pq:
        d, uy, ux = heapq.heappop(pq)

        if uy == N and ux == N:
            break

        for i in range(4):
            ny = uy + dy[i]
            nx = ux + dx[i]

            if -1 < ny < N and -1 < nx < N:
                if dist[ny][nx] > dist[uy][ux] + g[ny][nx]:
                    dist[ny][nx] = dist[uy][ux] + g[ny][nx]
                    heapq.heappush(pq, (dist[ny][nx], ny, nx))

    print('#%d %d' % (test_case, dist[N - 1][N - 1]))
