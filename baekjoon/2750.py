n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
for _ in range(n):
    print(arr[_])