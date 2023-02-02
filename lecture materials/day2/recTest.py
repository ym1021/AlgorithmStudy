# for문으로 구현이 가능하다면 재귀함수는 비추
# 3중 for문 이상이면 재귀함수 가능
# 피보나치 수열 같은 경우에는 재귀함수 사용
'''def recF(n):
    a = 100
    print(n)
    recF(n+1)

recF(1)'''

# fibo 초기값 2개 선언, 0 : 0 1: 1 f(n-1)+f(n-2) n>1
recCnt = 0
def fibo(n):
    global recCnt
    recCnt += 1
    if n<2:
        return n
    return fibo(n-1)+fibo(n-2)

dpcnt = 0
dpmemo = [0]*101
def fibo_rec_dp(n):
    global dpcnt
    dpcnt+=1
    if n<2:
        return n
    if dpmemo[n] == 0:
        dpmemo[n] = fibo_rec_dp(n-1)+fibo_rec_dp(n-2)
    return dpmemo[n]

idx = 5
print('fibo({}) = {}'.format(idx, fibo(idx)))
print('fibo_dp({}) = {}'.format(idx, fibo_rec_dp(idx)))
print(recCnt)
print(dpcnt)

