import sys

num = int(input())
for i in range(0, num):
    x = sys.stdin.readline().rstrip()
    y = list(map(int, x.split()))
    print(y[0]+y[1])
