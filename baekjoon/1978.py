num = int(input())
arr = list(map(int, input().split()))
res = 0
for _ in range(num):
    for i in range(2, arr[_]+1):
        if arr[_] % i == 0:
            if arr[_] == i:
                res += 1
            break
print(res)
