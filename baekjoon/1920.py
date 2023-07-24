import sys
input_ = sys.stdin.readline

n = int(input())
nset = set(map(int, input_().split()))
m = int(input())
arr = list(map(int, input_().split()))

for _ in arr:
    print(1) if _ in nset else print(0)