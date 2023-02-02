# 정올 1816 외양간 (탐욕알고리즘)

'''m, s, c = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(c)]
sub = []
for i in range(c):
    sub[i] = data[i+1] - data[i] - 1

print(data)'''

import sys
sys.stdin = open('../../files/input.txt', 'r')

M, S, C = map(int, input().split())
rooms = []
minus = []
for _ in range(C):
    rooms.append(int(input()))

if M<C:
    rooms.sort()
    for i in range(1, C):
        minus.append(rooms[i]-rooms[i-1]-1)
    minus.sort()
    ans = rooms[-1] - rooms[0] + 1
    for i in range(-1, -M, -1):
        ans -= minus[i]
    print(ans)
else:
    print(C)
