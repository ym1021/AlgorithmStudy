n = int(input())
step = [0] + [int(input()) for _ in range(n)] + [0]
dp = [0] * (n+2)
dp[1] = step[1]
dp[2] = dp[1] + step[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2], dp[i-3] + step[i-1]) + step[i]
print(dp[n])