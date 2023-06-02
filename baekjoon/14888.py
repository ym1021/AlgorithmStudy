import sys
input_ = sys.stdin.readline

n = int(input_())
num = list(map(int, input_().split()))
op = list(map(int, input_().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, sub, multi, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth+1, total+num[depth], plus-1, sub, multi, divide)
    if sub:
        dfs(depth + 1, total - num[depth], plus, sub-1, multi, divide)
    if multi:
        dfs(depth + 1, total * num[depth], plus, sub, multi-1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, sub, multi, divide-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)