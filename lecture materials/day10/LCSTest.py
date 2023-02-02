#최대 공통 부분수열(LCS)

yStr = '0'+'abcde'
xStr = '0'+'akckkd'
yLen = len(yStr)
xLen = len(xStr)
dp = [[0]*xLen for _ in range(yLen)]

for i in dp:
    print(i)

for i in range(1, yLen):
    for j in range(1, xLen):
        if yStr[i] == xStr[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print('============================')
for i in dp:
    print(i)

print('lcs max :', dp[yLen-1][xLen-1])