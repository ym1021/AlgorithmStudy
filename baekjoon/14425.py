import sys
input_ = sys.stdin.readline

n, m = map(int, input_().split())
s = set()

for _ in range(n):
    s.add(input_())

res = 0
for _ in range(m):
    test = input_()
    if test in s:
        res += 1

print(res)