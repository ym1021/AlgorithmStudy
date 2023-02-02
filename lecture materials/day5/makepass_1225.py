'''import sys
sys.stdin = open('../files/input.txt', 'r', encoding='utf-8')
tc = 11

for testCase in range(1, tc):
    input()
    rowData = list(input().split())
    if rowData[-1] != 0:
        rowData[0], rowData[-1] = rowData[-1], rowData[0]
    print(rowData[0])'''

import sys
sys.stdin = open('../../files/input.txt', 'r')

from collections import deque
'''
for test_case in range(1, 2):
    input()
    dq = deque(map(int, input().split()))
    minV = min(dq)//15 * 15
    for i in range(8):
        dq[i] = dq[i] - minV + 15
    k = 0

    cnt = 0
    while dq[-1]:
        cnt+=1
        k = k % 5 + 1
        num = dq.popleft() - k
        if num < 0:
            num = 0
        dq.append(num)
    ans = ''
    for i in dq:
        ans = ans + str(i) + ' '
    print('#%d %s' % (test_case, ans))
    print('cnt : ', cnt)
'''

for test_case in range(1, 2):
    input()
    dq = deque(map(int, input().split()))
    k = 0
    cnt = 0
    while dq[-1]:
        cnt+=1
        k = k % 5 + 1
        num = dq.popleft() - k
        if num < 0:
            num = 0
        dq.append(num)
    ans = ''
    for i in dq:
        ans = ans + str(i) + ' '
    print('cnt :', cnt)
    print('#%d %s' % (test_case, ans))
#    print('#%d %s' % (test_case, ' '.join(map(str, dq))))

