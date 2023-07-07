import sys
input_ = sys.stdin.readline

n, k = map(int, input_().split())
arr = list(map(int, input_().split()))
temp = sum(arr[:k])
res = temp

for i in range(k, n):
    temp += arr[i] - arr[i-k]
    res = max(res, temp)

print(res)