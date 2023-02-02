import sys
sys.stdin = open('../../files/input.txt', 'r')

V, E = map(int, input().split())
g = [[] for _ in range(V+1) ]

for _ in range(E):
    sn, en = map(int, input().split())
    g[sn].append(en)
    g[en].append(sn)
'''   
for i in range(1, V+1):
    print('%d :[' % i, end='')
    for j in g[i]:
        print(j, end=' ')
    print(']')
'''

stk = []
visited = [1]*(V+1)

stk.append(1)
visited[1] = 0
print('dfs : [', end='')
while stk:
    u = stk.pop()
    print(u, end=' ')
    for i in g[u]:
        if visited[i]:
            stk.append(i)
            visited[i] = 0
print(']')
















