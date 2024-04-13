import sys

n = int(sys.stdin.readline())

for _ in range(n):
    temp = []
    PS = list(sys.stdin.readline().strip())
    for i in range(len(PS)):
        if PS[i] == '(':
            temp.append('(')
        elif PS[i] == ')':
            if temp:
                temp.pop()
            else:
                temp.append(')')
                break
    if temp:
        print("NO")
    else:
        print("YES")