import sys
sys.stdin = open('../../files/input.txt', 'r')

INF = 987654321

def btr(k, idx, dist):
    global mindist
    if mindist < dist:
        return
    if k == N:
        dist += g[idx][k+1]
        if mindist > dist:
            mindist = dist
        return
    k += 1
    for i in range(1, N+1):
        if visited[i]:
            visited[i] = False
            btr(k, i, dist+g[idx][i])
            visited[i] = True

tc = int(input())+1
for testCase in range(1, tc):
    mindist = INF
    N = int(input())
    data = list(map(int, input().split()))
    customX = [data[0]]
    customY = [data[1]]
    for i in range(4, (N+2)*2, 2):
        customX.append(data[i])
        customY.append(data[i+1])
    customX.append(data[2])
    customY.append(data[3])
    g = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+1):
        for j in range(N+2):
            g[i][j] = g[j][i] = \
                abs(customX[i]-customX[j])+abs(customY[i]-customY[j])
    visited = [True]*(N+2)
    btr(0,0,0)
    print('#%d %d' % (testCase, mindist))
