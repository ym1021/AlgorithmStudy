#연속행렬곱셉(MCM)
def mcm_iter():
    for L in range(1, N):
        for s in range(1, N - L + 1):
            e = s + L
            dp[s][e] = 987654321
            for k in range(s, e):
                tmp = dp[s][k] + dp[k + 1][e] \
                      + sortedMatrix[s - 1] * sortedMatrix[k] * sortedMatrix[e]
                if dp[s][e] > tmp:
                    dp[s][e] = tmp
    return dp[1][N]

def mcm_rec(s, e):
    if dp[s][e] or s==e:
        return dp[s][e]

    dp[s][e] = 987654321
    for k in range(s, e):
        tmp = mcm_rec(s,k) + mcm_rec(k + 1,e) \
              + sortedMatrix[s - 1] * sortedMatrix[k] * sortedMatrix[e]
        if dp[s][e] > tmp:
            dp[s][e] = tmp
    return dp[s][e]


N = 4
matrix = [(2,3),(3,6),(6,5), (5,4)]
sortedMatrix = [2,3,6,5,4]

dp = [[0]*(N+1) for _ in range(N+1)]


#print('mcm_iter min : ', mcm_iter())
print('mcm_rec min : ', mcm_rec(1,N))