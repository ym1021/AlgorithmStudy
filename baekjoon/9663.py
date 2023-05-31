def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == abs(x-i):
            return False
    return True

def dfs(x):
    global res
    if x == n:
        res += 1
        return
    for i in range(n):
        col[x] = i
        if check(x):
            # print(x, " ", i)
            dfs(x+1)

n = int(input())
res = 0
col = [0]*15

dfs(0)
print(res)