import sys
sys.stdin = open('../../files/input.txt', 'r')

from queue import PriorityQueue
def dijkstra1(start, end):
    dist = [INF]*(V+1)
    visited = [True]*(V+1)
    dist[start] = 0

    for _ in range(1, V):#반복의 횟수 : V(7개)이면 6번 반복
        mindist = INF
        u = -1
        for i in range(1, V+1):
            if visited[i] and mindist>dist[i]:
                mindist = dist[i]
                u = i
        if u == end: break
        visited[u] = False

        for eIdx, val in g[u]:
            if dist[eIdx] > dist[u] + val:
                dist[eIdx] = dist[u] + val

    print('idx :\t[', end='')
    for i in range(1, V + 1):
        print(i, end='\t')
    print(']')
    print('dist :\t[', end='')
    for i in range(1, V + 1):
        print(dist[i], end='\t')
    print(']')

def dijkstra2(start, end):
    dist = [INF]*(V+1)
    p = [0]*(V+1)
    pq = PriorityQueue()
    dist[start] = 0
    #(거리, 노드번호)
    pq.put((0,start))

    while not pq.empty():
        _, idx = pq.get()
        if idx == end: break
        for eIdx, val in g[idx]:
            if dist[eIdx] > dist[idx]+val:
                dist[eIdx] = dist[idx]+val
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

def dijkstra3(start, end):
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
        if idx == end: break
        visited[idx] = False
        for eIdx, val in g[idx]:
            if visited[eIdx] and dist[eIdx] > dist[idx]+val:
                dist[eIdx] = dist[idx]+val
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

dijkstra3(1, 7)