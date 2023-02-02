data = [0,'a','b','c']
n = 3
r = 2  # depth
a = [0]*(n+1)
visited = [True]*(n+1)

def myPrint():
    print('[', end='')
    for i in range(1, r+1):
        print(data[a[i]], end=' ')
    print(']')

def btr_perm(k):
    if k == r:
        myPrint()
        return
    k+=1
    for i in range(1, n+1):
        if visited[i]:
            visited[i] = False
            a[k] = i
            btr_perm(k)
            visited[i] = True
def btr_pi(k):
    if k == r:
        myPrint()
        return
    k+=1
    for i in range(1, n+1):
        a[k] = i
        btr_pi(k)


btr_perm(0)
print('===========')
btr_pi(0)


