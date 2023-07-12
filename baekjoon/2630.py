import sys
input_ = sys.stdin.readline

n = int(input_())
paper = [list(map(int, input_().split())) for _ in range(n)]

res = [0, 0]

def sol(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                sol(x, y, n//2)
                sol(x, y+n//2, n//2)
                sol(x+n//2, y, n//2)
                sol(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        res[0] += 1
    else:
        res[1] += 1
sol(0, 0, n)
for _ in res:
    print(_)