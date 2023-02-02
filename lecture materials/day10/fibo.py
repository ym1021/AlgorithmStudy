size = 101
dp1 = [0]*size
def fibo_rec(n):
    if n < 2:
        return n
    if dp1[n] == 0:
        dp1[n] = fibo_rec(n-1) + fibo_rec(n-2)
    return dp1[n]

dp2 = [0]*size
def fibo_iter(n):
    dp2[1] = 1
    for i in range(2, n+1):
        dp2[i] = dp2[i-1]+dp2[i-2]
    return dp2[n]
dp3 = [0]*3
def fibo_iter2(n):
    dp3[1] = 1
    for i in range(2, n+1):
        dp3[i%3] = dp3[(i-1)%3]+dp3[(i-2)%3]
    return dp3[n%3]

n = 1000
#print('fibo_rec(%d) = %d' % (n, fibo_rec(n)))
#print('fibo_iter(%d) = %d' % (n, fibo_iter(n)))
print('fibo_iter2(%d) = %d' % (n, fibo_iter2(n)))