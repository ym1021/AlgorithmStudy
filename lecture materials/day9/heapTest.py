#최소힙
N = 5
heap = [0]*(N+1)
top = 0

def push(data):
    global top
    top+=1
    heap[top] = data
    idx = top
    while True:
        if idx==1 or heap[idx//2] < heap[idx]:
            break
        heap[idx // 2], heap[idx] =  heap[idx], heap[idx//2]
        idx = idx//2

def pop():
    global top
    val = heap[1]
    heap[1] = heap[top]
    top -= 1
    idx = 1
    next = -1
    while True:
        next = idx*2
        if next<top and heap[next] > heap[next+1]:
            next+=1
        if next > top or heap[idx] < heap[next]:
            break

        heap[idx], heap[next] = heap[next], heap[idx]
        idx = next

    return val

def myPrint():
    print('[', end='')
    for i in range(1, top+1):
        print(heap[i], end=' ')
    print(']')

myPrint()
push(100)
myPrint()
push(300)
myPrint()
push(50)
myPrint()
push(60)
myPrint()
push(200)
myPrint()
#isFull
if top < N:
    push(3)
    myPrint()



print('pop :', pop())
myPrint()
print('pop :', pop())
myPrint()
print('pop :', pop())
myPrint()
print('pop :', pop())
myPrint()
print('pop :', pop())
myPrint()
print('end1')
#isEmpty
if top:
    print('pop :', pop())
    myPrint()
print('end2')
