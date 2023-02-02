# import sys
# sys.stdin = open('../files/input.txt', 'r')
#
# for testCase in range(1, 2):
#     left = [-1] * 100
#     right = [-1] * 100
#
#     _, cnt = map(int, input().split())
#     data = list(map(int, input().split()))
#
#     for i in range(0, cnt*2, 2):
#         pass

import sys
sys.stdin = open('../../files/input.txt', 'r')

for testCase in range(1, 11):
    _, cnt = map(int, input().split())
    data = list(map(int, input().split()))
    g =[[] for _ in range(100)]

    for i in range(0, cnt*2, 2):
        g[data[i]].append(data[i+1])

    stk = []
    stk.append(0)
    flag = False
    while stk:
        u = stk.pop()
        if u == 99:
            flag = True
            break
        for i in g[u]:
            stk.append(i)
    print('#%d %d' % (testCase, flag))