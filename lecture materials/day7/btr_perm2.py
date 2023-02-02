data = [0,'a','b','c']
n = 3
r = 2#depth
a = [0]*(n+1)

def myPrint():
    print('[', end='')
    for i in range(1, r + 1):
        print(data[a[i]], end=' ')
    print(']')

def makeCandidates(k):
    inPerm = [True]*(n+1)
    for i in range(1, k):
        inPerm[a[i]] = False
    _list = []
    for i in range(1, n+1):
        if inPerm[i]:
            _list.append(i)
    return _list

def btr_perm(k):
    if k == r:
        myPrint()
        return
    k+=1
    _list = makeCandidates(k)
    for i in _list:
        a[k] = i
        btr_perm(k)

btr_perm(0)
