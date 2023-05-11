import sys
input_ = sys.stdin.readline

n, m = map(int, input_().split())
s = set()
chk = set()

for _ in range(n):
    s.add(input_().rstrip())

for _ in range(m):
    chk.add(input_().rstrip())

res = sorted(list(s & chk))

print(len(res), *res, sep="\n")