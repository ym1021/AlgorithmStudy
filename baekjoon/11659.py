import sys
input_ = sys.stdin.readline

n, m = map(int, input_().split())
arr = list(map(int, input_().split()))
pfs = [0]

temp = 0
for _ in arr:
    temp += _
    pfs.append(temp)

# print(pfs)
for _ in range(n):
    a, b = map(int, input_().split())
    print(pfs[b]-pfs[a-1])
