import sys
sys.stdin = open('../../files/input.txt', 'r')

XMODE = 1
YMODE = 2
resultCnt = 987654321
dy = [-1,1,0,0]
dx = [0,0,-1,1]

M, N = map(int, input().split())
m, n = map(int, input().split())
endY = m+1
endX = n+1
data = [[0]*(N+2)]
for i in range(1,M+1):
    data.append([0])
    data[i].extend(list(map(int, input().split())))
    data[i].append(0)
data.append([0]*(N+2))

dist = [[0]*(N+2)]
for i in range(1,M+1):
    dist.append([0])
    dist[i].extend([987654321]*(N))
    dist[i].append(0)
dist.append([0]*(N+2))


stk = []
dist[1][1] = 0
if data[1][2]:
    dist[1][2] = 0
    #(y, x, mode, cnt)
    stk.append((1,2, XMODE, 0))
    while stk:
        u = stk.pop()
        for i in range(4):
            ny = u[0] + dy[i]
            nx = u[1] + dx[i]
            if data[ny][nx]:
                if i<2:
                    mode2 = YMODE
                else:
                    mode2 = XMODE
                if u[2] == mode2:
                    cnt = u[3]
                else:
                    cnt = u[3]+1
                if dist[ny][nx] > cnt:
                    dist[ny][nx] = cnt
                    stk.append((ny, nx, mode2, cnt))

if data[2][1]:
    dist[2][1] = 0
    stk.append((2,1, YMODE, 0))
    while stk:
        u = stk.pop()
        for i in range(4):
            ny = u[0] + dy[i]
            nx = u[1] + dx[i]
            if data[ny][nx]:
                if i<2:
                    mode2 = YMODE
                else:
                    mode2 = XMODE
                if u[2] == mode2:
                    cnt = u[3]
                else:
                    cnt = u[3]+1
                if dist[ny][nx] > cnt:
                    dist[ny][nx] = cnt
                    stk.append((ny, nx, mode2, cnt))

print(dist[endY][endX])
