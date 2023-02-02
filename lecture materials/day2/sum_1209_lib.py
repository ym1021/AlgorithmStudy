import sys
sys.stdin = open('../../files/input.txt', 'r')
tc = 11

for testCase in range(1, tc):
    input()
    rowData = [list(map(int, input().split())) for _ in range(100)]
    colData = list(zip(*rowData))
    #colData = list(list(i) for i in zip(*rowData))

    ans = []

    for i in rowData:
        ans.append(sum(i))
    for i in colData:
        ans.append(sum(i))

    result = 0
    for i in range(100):
        result+=rowData[i][i]
    ans.append(result)

    result = 0
    for i in range(100):
        result += rowData[i][99-i]
    ans.append(result)

    print('#%d %d' % (testCase, max(ans)))