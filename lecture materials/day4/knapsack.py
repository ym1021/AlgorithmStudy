jw = [0,10,25,15]
jp = [0,10,20,14]
N = 3
W = 30

#보석이 무한개
dp1 = [0]*(W+1)
def knap1():
    iLen = W+1
    jLen = N+1
    for i in range(1, iLen):#가방
        for j in range(1, jLen):#보석
            if i >= jw[j]:#공간 확보
                if dp1[i] < dp1[i-jw[j]] + jp[j]:
                    dp1[i] = dp1[i - jw[j]] + jp[j]
 #   return dp1[W]

#보석이 1개
dp2 = [[0]*(W+1) for _ in range(N+1)]
def knap2():
    iLen = N+1
    jLen = W+1
    for i in range(1, iLen):#보석
        for j in range(1, jLen): #가방
            dp2[i][j] = dp2[i-1][j]
            if jw[i] <= j:
                if dp2[i][j] < dp2[i-1][j-jw[i]] + jp[i]:
                    dp2[i][j] = dp2[i-1][j-jw[i]] + jp[i]

#print('knap1_1 : %d' % knap1())
knap1()
print('knap1_2 : %d' % dp1[W])
knap2()
print('knap2 : %d' % dp2[N][W])
