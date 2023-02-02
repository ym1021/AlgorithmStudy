n = 100
data = [i for i in range(n+1)]
key = 1250
a = [0]*(n+1)

resultCnt = 0
recCnt = 0
def btr_subset(k, sum):
    global resultCnt
    if sum > key:
        return
    if k == n:
        if sum==key:
            resultCnt+=1
        return
    k+=1
    btr_subset(k, sum)
    btr_subset(k, sum+data[k])
def btr_subset1(k, sum, restSum):
    global resultCnt
    global recCnt
    recCnt+=1
    if sum+restSum < key:
        return
    if sum > key:
        return
    if k == n:
        if sum==key:
            resultCnt+=1
        return
    k+=1
    btr_subset1(k, sum, restSum-data[k])
    btr_subset1(k, sum+data[k], restSum-data[k])
def btr_subset2(k, sum, restSum):
    global resultCnt
    global recCnt
    recCnt += 1
    if sum+restSum < key:
        return
    if sum > key:
        return
    if sum == key:
        resultCnt += 1
        return
    if k == n:
        return
    k+=1
    btr_subset2(k, sum, restSum-data[k])
    btr_subset2(k, sum+data[k], restSum-data[k])

restSum = 0
for i in range(1, n+1):
    restSum+=data[i]
btr_subset2(0,0, restSum)
print('recCnt :', recCnt)
print('resultCnt :', resultCnt)