data = [0,'a','b','c']
temp = [0]*len(data)
n = 3
r = 2
def myPrint():
    print('[', end='')
    for i in range(1, r+1):
        print(temp[i], end=' ')
    print(']')

def perm(n, r):
    if r==0:
        myPrint()
        return
    for i in range(n, 0, -1):
        data[n], data[i] = data[i], data[n]
        temp[r] = data[n]
        perm(n-1, r-1)
        data[n], data[i] = data[i], data[n]
'''
def pi(n, r):
    if r==0:
        myPrint()
        return
    for i in range(n, 0, -1):
        data[n], data[i] = data[i], data[n]
        temp[r] = data[n]
        pi(n, r-1)
        data[n], data[i] = data[i], data[n]
'''
def pi(n, r):
    if r==0:
        myPrint()
        return
    for i in range(n, 0, -1):
        temp[r] = data[i]
        pi(n, r-1)

def comb(n, r):
    if r==0:
        myPrint()
        return
    if n<r:
        return
    temp[r] = data[n]
    comb(n-1, r-1)
    comb(n-1, r)

def H(n, r):
    if r==0:
        myPrint()
        return
    if n==0:
        return
    temp[r] = data[n]
    H(n, r-1)
    H(n-1, r)
'''
perm(n, r)
print('============')
pi(n,r)
print('============')
comb(n,r)
print('============')
H(n,r)
'''

def comb_cal(n, r):
    if r == 0:
        return 1
    if n == r:
        return 1
    return comb_cal(n-1, r-1)+comb_cal(n-1, r)
'''
for i in range(n+1):
    r = i
    comb(n, r)'''
dpMemo = [[0]*101 for _ in range(101)]
def comb_cal_dp(n, r):
    if r == 0:
        return 1
    if n == r:
        return 1
    if dpMemo[n][r] == 0:
        dpMemo[n][r] = comb_cal_dp(n-1, r-1)+comb_cal_dp(n-1, r)
    return dpMemo[n][r]
n = 100
r = 50
print('%d C %d = %d' % (n, r, comb_cal_dp(n,r)))