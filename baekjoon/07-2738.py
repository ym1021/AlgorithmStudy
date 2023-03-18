a, b = [], []
n, m = map(int, input().split())

for _ in range(n):
    _ = list(map(int, input().split()))
    a.append(_)

for _ in range(n):
    _ = list(map(int, input().split()))
    b.append(_)

for row in range(n):
    for col in range(m):
        print(a[row][col]+b[row][col], end=' ')
    print()