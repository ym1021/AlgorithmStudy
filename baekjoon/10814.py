import sys
input_ = sys.stdin.readline

n = int(input_())
arr = []

for _ in range(n):
    x, y = map(str, input_().split())
    arr.append([x, y])

arr.sort(key = lambda x : int(x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])
