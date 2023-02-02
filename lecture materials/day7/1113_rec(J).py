import sys
sys.stdin = open('../../files/input.txt', 'r')

XMODE = 1
YMODE = 2
resultCnt = 987654321
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def chk(y, x, mode, cnt):
    global resultCnt
    data[y][x] = 0
    if cnt > resultCnt: #가지치기
        data[y][x] = 1
        return
    if y == endY and x == endX: # 결정 났을때의 리턴
        if cnt<resultCnt:
            resultCnt = cnt
        data[y][x] = 1
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if data[ny][nx]:
            if i<2:
                mode2 = YMODE
            else:
                mode2 = XMODE
            if mode == mode2:
                chk(ny, nx, mode2, cnt)
            else:
                chk(ny, nx, mode2, cnt+1)
    data[y][x] = 1

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

data[1][1] = 0
if data[1][2]:
    chk(1,2, XMODE, 0)
if data[2][1]:
    chk(2,1, YMODE, 0)

print(resultCnt)

