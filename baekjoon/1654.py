import sys
input_ = sys.stdin.readline
k, n = map(int, input_().split())
lan = [int(input_()) for _ in range(k)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lan:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
    print(lines, mid, start, end)
print(end)