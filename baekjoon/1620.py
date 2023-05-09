import sys
input_ = sys.stdin.readline

n, m = map(int, input_().split())
poket = {}

for i in range(1, n+1):
    b = input_().rstrip()
    poket[i] = b
    poket[b] = i

for _ in range(m):
    res = input_().rstrip()
    if res.isdigit():
        print(poket[int(res)])
    else:
        print(poket[res])