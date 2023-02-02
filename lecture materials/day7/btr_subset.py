data = [0,'a','b','c']
n = 3
a = [0]*(n+1)

def myPrint():
    print('{', end='')
    for i in range(1, n+1):
        if a[i]:
            print(data[i], end=' ')
    print('}')
'''
def btr_subset(k):
    if k == n:
        myPrint()
        return
    k+=1
    for i in range(2):
        a[k] = i
        btr_subset(k)
'''
def btr_subset(k):
    if k == n:
        myPrint()
        return
    k+=1
    a[k] = 0
    btr_subset(k)
    a[k] = 1
    btr_subset(k)

btr_subset(0)