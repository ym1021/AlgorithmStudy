num = int(input())
arr = list(map(int, input().split()))
top = max(arr)
newarr = []
for _ in arr:
    newarr.append(_/top*100)
avg = sum(newarr)/num
print(avg)