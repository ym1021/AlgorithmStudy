'''
queue : FIFO
graph : bfs(너비우선탐색) => 최단경로 => dijkstra (우선순위큐)
절대 list사용 하지 않는다
'''
'''
que = []
que.append(100)
que.append(200)
que.append(300)
print(que)
print('pop : ', que.pop(0))
print(que)
'''
'''
from queue import Queue, PriorityQueue
q = Queue()
q.put(100)
q.put(200)
q.put(300)'''
'''
for i in q:
    print(i)
    '''
'''
while not q.empty():
    print(q.get())
'''
'''
from collections import deque
dq = deque()
dq.append(100)
dq.append(200)
print(dq)
dq.appendleft(300)
print(dq)

print('pop : ', dq.pop())
print(dq)
print('pop : ', dq.popleft())
print(dq)'''

#우선순위큐 => heapTree를 기점으로 만듬
#python => 작은값 먼저 나옴
#from queue import PriorityQueue
#pq = PriorityQueue()
'''
pq.put(3)
pq.put(2)
pq.put(8)
pq.put(1)
while not pq.empty():
    print(pq.get())
'''
'''
pq.put((2,100))
pq.put((3,300))
pq.put((1,500))
pq.put((4,400))
while not pq.empty():
    print(pq.get())
'''
#선형큐
qsize = 5
que = [0]*qsize
front = 0
rear = 0
que[rear] = 100
rear+=1
que[rear] = 200
rear+=1
que[rear] = 300
rear+=1
que[rear] = 400
rear+=1
que[rear] = 500
rear+=1

for i in range(front, rear):
    print(que[i])
'''
print('pop : ', que[front])
front+=1

for i in range(front, rear):
    print(que[i])'''
print('=============')
while front!=rear:
    print(que[front])
    front+=1