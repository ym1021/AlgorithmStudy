import sys
sys.stdin = open('../../files/input.txt', 'r')
tc = 11
for testCase in range(1, 2):
    N = int(input())
    data = [0]*(N+1)
    # op,num,leftC, rightC
    for i in range(N):
        idx, *d = input().split()
        if d[0] == '+' or d[0] == '-' or d[0] == '*' or d[0] == '/':
            data[int(idx)] = [d[0], 0, int(d[1]), int(d[2])]
        else:
            data[int(idx)] = [0, int(d[0]), -1, -1]
    print(data)
