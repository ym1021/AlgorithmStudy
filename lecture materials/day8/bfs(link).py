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
        for eIdx, val in g[u]:
            if dist[eIdx] > dist[u]+val:
                dist[eIdx] = dist[u]+val
                q.append(eIdx)
                p[eIdx] = u

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


INF = 987654321
V, E = map(int, input().split())
g = [[] for _ in range(V+1)]
print(g)
for i in range(E):
    sn, en, val = map(int, input().split())
    g[sn].append((en, val))
'''
for i in g:
    for j in i:
        print(j,end=' ')
    print()
'''

bfs(1)