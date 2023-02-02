'''
7 11
1 2 32
1 3 31
1 6 60
1 7 51
2 3 21
3 5 46
3 7 25
4 5 34
4 6 18
5 6 40
5 7 51
'''

import sys
sys.stdin = open('../../files/input.txt', 'r')

from queue import PriorityQueue

def prim(start):
    dist = [INF]*(V+1)
    p = [0]*(V+1)
    visited = [True]*(V+1)
    pq = PriorityQueue()
    dist[start] = 0
    #(거리, 노드번호)
    pq.put((0,start))

    while not pq.empty():
        _, idx = pq.get()
        if not visited[idx]: continue

        visited[idx] = False
        for eIdx, val in g[idx]:
            if visited[eIdx] and dist[eIdx] > val:
                dist[eIdx] = val
                pq.put((dist[eIdx],eIdx))
                p[eIdx] = idx

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
    g[en].append((sn, val))
'''
for i in g:
    print('[', end='')
    for j in i:
        print(j, end=' ')
    print(']')
'''
prim(2)
