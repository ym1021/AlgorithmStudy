import sys
sys.stdin = open('../../files/input.txt', 'r')
#in chk
def dfs1(start):
    visited = [1] * (V + 1)
    stk = []

    # in chk
    stk.append(start)
    visited[start] = 0
    print('dfs1 : [', end='')
    while stk:
        n = stk.pop()
        print(n, end=' ')
        for i in range(1, V + 1):
            if g[n][i] and visited[i]:
                stk.append(i)
                visited[i] = 0
    print(']')
#out chk
def dfs2(start):
    visited = [1] * (V + 1)
    stk = []

    # out chk
    stk.append(start)
    print('dfs2 : [', end='')
    while stk:
        n = stk.pop()
        if visited[n]:
            visited[n] = 0
            print(n, end=' ')
            for i in range(1, V + 1):
                if g[n][i] and visited[i]:
                    stk.append(i)
    print(']')


def dfs_rec(start):
    print(start, end=' ')
    visitedMain[start] = 0
    for i in range(V+1):
        if g[start][i] and visitedMain[i]:
            dfs_rec(i)



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

dfs1(1)
dfs2(1)
print('dfs_rec : [', end='')
dfs_rec(1)
print(']')
