import sys
sys.stdin = open('../../files/input.txt', 'r')
tc = int(input())+1
for testCase in range(1, 2):
    V, E, S1, S2 = map(int, input().split())
    leftC = [0]*(V+1)
    rightC = [0]*(V+1)
    p = [0]*(V+1)
    data = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        if leftC[data[i]]:
            rightC[data[i]] = data[i+1]
        else:
            leftC[data[i]] = data[i+1]
        p[data[i+1]] = data[i]

    print(leftC)
    print(rightC)
    print(p)

