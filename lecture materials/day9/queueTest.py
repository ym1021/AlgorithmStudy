def myPrint():
    global front, rear
    print('queue :[', end='')
    for i in range(front, rear):
        print(que[i], end=' ')
    print(']')

N = 5
que = [0]*N
front = 0
rear = 0

que[rear] = 1
rear+=1
que[rear] = 2
rear+=1
que[rear] = 3
rear+=1
que[rear] = 4
rear+=1
que[rear] = 5
rear+=1
myPrint()
if rear<N:
    que[rear] = 100
    rear+=1
print(front, rear)
myPrint()

print('pop :', que[front])
front+=1
myPrint()
print('pop :', que[front])
front+=1
myPrint()
print('pop :', que[front])
front+=1
myPrint()
print('pop :', que[front])
front+=1
myPrint()
print('pop :', que[front])
front+=1
myPrint()
print('end1')
if front!=rear:
    print('pop :', que[front])
    front += 1
    myPrint()
print('end2')