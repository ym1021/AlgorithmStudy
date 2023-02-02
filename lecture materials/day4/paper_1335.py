# 정올 1335 색종이 만들기(영역구분) (분할정복)

'''m, s, c = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(c)]
sub = []
for i in range(c):
    data

print(data)'''

import sys
#sys.stdout = open('out.txt', 'w')
sys.stdin = open('../../files/input.txt', 'r')
N = int(input())
mapData = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
def check(y, x, n):
  #  print(y, x, n)
    global white
    global blue
    temp = mapData[y][x]
    flag = True
    for i in range(y, y+n):
        if not flag:
            break
        for j in range(x, x+n):
            if temp != mapData[i][j]:
                flag = False
                break
    if flag:
        if temp:
            blue+=1
        else:
            white+=1
    else:
        check(y,x, n//2)#위, 왼
        check(y, x+n//2, n//2)#위, 오
        check(y+n//2, x, n//2)#아, 왼
        check(y+n//2, x+n//2, n//2)#아, 오


check(0,0,N)
print(white)
print(blue)


