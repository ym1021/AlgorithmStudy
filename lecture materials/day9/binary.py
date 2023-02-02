#전위, 후위 : 루트의 위치
#중위 : 왼쪽 개수, 오른쪽 개수
#이진탐색트리를 중위순회 접근 오름차순
from collections import deque
'''
def bfs(start):
    q = deque()
    q.append(start)
    print('bfs : [', end='')
    while q:
        u = q.popleft()
        print(data[u], end=' ')
        for i in range(2):
            if data[u*2+i]:
                q.append(u*2+i)
    print(']')
'''
def bfs(start):
    q = deque()
    q.append(start)
    print('bfs : [', end='')
    while q:
        u = q.popleft()
        print(data[u], end=' ')
        if data[u*2]:
            q.append(u*2)
        if data[u * 2 + 1]:
            q.append(u * 2 + 1)
    print(']')

def prePrint1(root):
    if data[root]:
        print(data[root], end=' ')
        prePrint1(root*2)
        prePrint1(root*2+1)
def prePrint2(root):
    if not data[root]:
        return
    print(data[root], end=' ')
    prePrint2(root*2)
    prePrint2(root*2+1)
def prePrint3(root):
    if root:
        print(data[root], end=' ')
        prePrint3(leftC[root])
        prePrint3(rightC[root])

def inPrint(root):
    if data[root]:
        inPrint(root*2)
        print(data[root], end=' ')
        inPrint(root*2+1)
def postPrint(root):
    if data[root]:
        postPrint(root*2)
        postPrint(root*2+1)
        print(data[root], end=' ')

N = 10
data = [0]*((N+1)*2)
for i in range(1, N+1):
    data[i] = chr(64+i)
leftC = [0,2,4,6,8,10,0,0,0,0,0]
rightC = [0,3,5,7,9,0,0,0,0,0,0]
bfs(1)
print('pre1 : [', end='')
prePrint1(1)
print(']')
print('pre2 : [', end='')
prePrint2(1)
print(']')
print('pre3 : [', end='')
prePrint3(1)
print(']')
print('in : [', end='')
inPrint(1)
print(']')
print('post : [', end='')
postPrint(1)
print(']')

