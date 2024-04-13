import sys

stack = []
sum = 0

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == '0':
        stack.pop()
    else:
        stack.append(int(cmd[0]))

for i in stack:
    sum += i
print(sum)