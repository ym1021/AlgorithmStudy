import sys
sys.stdin = open('../../files/input.txt', 'r')
#고객이 15개 이상이면 반드시 D/P (TSP)
INF = 987654321
mindist = INF

def btr(k, idx, dist):
    global mindist
    if mindist < dist:
        return
    if k == N-1:
        dist += g[idx][0]
        if mindist > dist:
            mindist = dist
        return
    k += 1
    for i in range(1, N):
        if visited[i]:
            visited[i] = False
            btr(k, i, dist+g[idx][i])
            visited[i] = True


N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]
visited = [True]*N
'''
for i in g:
    for j in i:
        print(j, end=' ')
    print()'''
for i in range(N):
    for j in range(N):
        if i!=j and g[i][j] == 0:
            g[i][j] = INF

btr(0,0,0)

print(mindist)