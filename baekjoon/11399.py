n = int(input())
peo = list(map(int, input().split()))

peo.sort()
res = 0

for _ in range(1, n+1):
    res += sum(peo[0:_])
print(res)