n = int(input())
numList = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in range(0, n):
    if numList[i] == v:
        cnt += 1
print(cnt)
