num = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(num):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

res = 0
for _ in paper:
    res += _.count(1)
print(res)