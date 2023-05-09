import sys
input_ = sys.stdin.readline

n = int(input_())
temp = dict()

for _ in range(n):
    a, b = map(str, input_().split())
    if b == 'enter':
        temp[a] = b
    else:
        del temp[a]

temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)
