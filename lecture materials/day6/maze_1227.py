import sys
sys.stdin = open('../../files/input.txt', 'r')
#상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for testCase in range(1, 11):
    input()
    g = [list(input()) for _ in range(100)]

    flag = False
    sY = -1
    sX = -1
    for i in range(100):
        for j in range(100):
            if g[i][j] == '2':
                sY = i
                sX = j
                flag = True
                break
        if flag:
            break
#    print(sY, sX)
    stk = []
    stk.append(sY)
    stk.append(sX)
    g[sY][sX] = '1'
    flag = False
    while stk:
        cX = stk.pop()
        cY = stk.pop()
        if g[cY][cX] == '3':
            flag = True
            break
        for i in range(4):
            nY = cY + dy[i]
            nX = cX + dx[i]
            if g[nY][nX] != '1':
                stk.append(nY)
                stk.append(nX)
                g[cY][cX] = '1'

    print('#%d %d' % (testCase, flag))