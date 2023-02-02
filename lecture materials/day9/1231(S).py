import sys
sys.stdin = open('../../files/input.txt', 'r')
tc = 11
for testCase in range(1, 2):
    N = int(input())
    data = [0]*((N+1)*2)
    for i in range(N):
        idx, *b = input().split()
        idx = int(idx)
        data[idx] = b[0]
    print(data)