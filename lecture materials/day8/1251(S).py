import sys
sys.stdin = open('../../files/input.txt', 'r')
from queue import PriorityQueue
tc = int(input())+1
for testCase in range(1, tc):
    V = int(input())
    X = []
    Y = []
    for i in map(int, input().split()):
        X.append(i)
    for i in map(int, input().split()):
        Y.append(i)
    E = float(input())
    g = [[0]*V for _ in range(V)]
    for i in range(V-1):
        for j in range(i+1, V):
            g[i][j]=g[j][i] = (X[i]-X[j])*(X[i]-X[j])+(Y[i]-Y[j])**2

    INF = 1000000*1000000*3
    dist = [INF]*V
    visited = [True]*V
    pq = PriorityQueue()
    dist[0] = 0
    pq.put((0, 0))
    while not pq.empty():
        val, eIdx = pq.get()
        if not visited[eIdx]: continue
        visited[eIdx] = False
        for i in range(V):
            if visited[i] and dist[i] > g[eIdx][i]:
                dist[i] = g[eIdx][i]
                pq.put((dist[i], i))
    ans = 0
    for i in dist:
        ans += i
    ans *= E
    print('#%d %.0f' % (testCase,ans))