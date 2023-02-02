'''
7 11
1 2 3
1 3 5
2 3 1
2 4 2
2 5 4
3 2 3
3 4 4
3 6 6
4 5 7
4 6 2
5 6 4
5 7 5
6 5 3
6 7 8
'''
import sys
sys.stdin = open('../../files/input.txt', 'r')

from collections import deque
def bfs(start):
    dist = [INF]*(V+1)
    p = [0]*(V+1)
    q = deque()
    dist[start] = 0
    q.append(start)

    while q:
        u = q.popleft()
        for i in range(1, V+1):
            if dist[i] > dist[u]+g[u][i]:
                dist[i] = dist[u] + g[u][i]
                q.append(i)
                p[i] = u

    print('idx :\t[', end='')
    for i in range(1, V+1):
       print(i, end='\t')
    print(']')
    print('dist :\t[', end='')
    for i in range(1, V + 1):
        print(dist[i], end='\t')
    print(']')
    print('p\t:\t[', end='')
    for i in range(1, V + 1):
        print(p[i], end='\t')
    print(']')

def f_w(start):
    for k in range(1, V+1): #경유지
        for s in range(1, V+1):#출발지
            for e in range(1, V+1):#도착지
                if g[s][e] > g[s][k]+g[k][e]:
                    g[s][e] = g[s][k] + g[k][e]

    print('idx :\t[', end='')
    for i in range(1, V + 1):
        print(i, end='\t')
    print(']')
    print('dist :\t[', end='')
    for i in range(1, V + 1):
        print(g[start][i], end='\t')
    print(']')


INF = 987654321
V, E = map(int, input().split())
g = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    sn, en, val = map(int, input().split())
    g[sn][en] = val
'''
for i in range(1, V+1):
    for j in range(1, V+1):
        print(g[i][j], end=' ')
    print()
'''
for i in range(1, V+1):
    for j in range(1, V+1):
        if i!=j and g[i][j]==0:
            g[i][j] = INF
'''
for i in range(1, V+1):
    for j in range(1, V+1):
        if g[i][j] == INF:
            print('-', end=' ')
        else:
            print(g[i][j], end=' ')
    print()
'''

bfs(1)
print('===============')
f_w(1)
