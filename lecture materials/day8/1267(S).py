import sys
sys.stdin = open('../../files/input.txt', 'r')
from collections import deque
tc = 11
for testCase in range(1, tc):
    V, E = map(int, input().split())
    g = [[] for _ in range(V+1)]
    indegree = [0]*(V+1)
    data = list(map(int, input().split()))
    for i in range(0,E*2, 2):
        g[data[i]].append(data[i+1])
        indegree[data[i+1]] += 1

#    stk = []
    q = deque()
    for i in range(1, V+1):
        if indegree[i]==0:
  #          stk.append(i)
            q.append(i)
    print('#%d ' % testCase, end='')
#    while stk:
    while q:
#        u = stk.pop()
        u = q.popleft()
        print(u, end=' ')
        for i in g[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
  #              stk.append(i)
                q.append(i)
    print()

