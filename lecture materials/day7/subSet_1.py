n = 10
data = [i for i in range(n+1)]
key = 10
a = [0]*(n+1)
cnt = 0
resultCnt = 0
def myPrint():
    global cnt
    global resultCnt
    cnt+=1

    sum = 0
    for i in range(1, n+1):
        if a[i]:
            sum += data[i]

    if sum <= key:
        resultCnt+=1
        print('{', end='')
        for i in range(1, n+1):
            if a[i]:
                print(data[i], end=' ')
        print('}')

def btr_subset(k):
    if k == n:
        myPrint()
        return
    k+=1
    a[k] = 0
    btr_subset(k)
    a[k] = 1
    btr_subset(k)
def getSum(k):
    sum = 0
    for i in range(1, k+1):
        if a[i]:
            sum += data[i]
    return sum

def btr_subset1(k):
    if getSum(k) > key:
        return
    if k == n:
        myPrint()
        return
    k+=1
    a[k] = 0
    btr_subset1(k)
    a[k] = 1
    btr_subset1(k)
def btr_subset2(k, sum):
    if sum > key:
        return
    if k == n:
        myPrint()
        return
    k+=1
    a[k] = 0
    btr_subset2(k, sum)
    a[k] = 1
    btr_subset2(k, sum+data[k])
def btr_subset3(k, sum):
    global resultCnt
    if sum > key:
        return
    if k == n:
        resultCnt+=1
        return
    k+=1
  #  a[k] = 0
    btr_subset3(k, sum)
  #  a[k] = 1
    btr_subset3(k, sum+data[k])

btr_subset3(0,0)
print('cnt :', cnt)
print('reCnt :', resultCnt)