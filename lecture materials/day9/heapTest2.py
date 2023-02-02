#최소힙 (기준, 노드번호)
N = 5
heap = [0]*(N+1)
top = 0

def push(data):
    global top
    top+=1
    heap[top] = data
    idx = top
    while True:
        if idx==1 or heap[idx//2][0] < heap[idx][0]:
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
        if next<top and heap[next][0] > heap[next+1][0]:
            next+=1
        if next > top or heap[idx][0] < heap[next][0]:
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
push((2,200))
myPrint()
push((3,300))
myPrint()
push((1,100))
myPrint()
push((5,500))
myPrint()
push((4,400))
myPrint()

print('pop : ', pop())
myPrint()
print('pop : ', pop())
myPrint()
print('pop : ', pop())
myPrint()
print('pop : ', pop())
myPrint()
print('pop : ', pop())
myPrint()
