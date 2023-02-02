import sys
sys.stdin = open('../../files/input.txt', 'r', encoding='utf-8')
tc = 11

for testCase in range(1, tc):
    '''_ = input()
    arr = []
    res = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
    for i in range(100):
        sum1 = 0
        sum2 = 0
        for j in range(100):
            sum1 += arr[i][j]
            sum2 += arr[j][i]
        res.append(sum1)
        res.append(sum2)
    res.sort(reverse=True)

    print('#{} {}'.format(testCase, res[0]))'''

    input()
    rowData = [list(map(int, input().split())) for _ in range(100)]
    ans = 0

    for i in range(100):
        _sum = 0
        for j in range(100):
            _sum += rowData[i][j]
        if ans < _sum:
            ans = _sum
    for i in range(100):
        _sum = 0
        for j in range(100):
            _sum += rowData[j][i]
        if ans < _sum:
            ans = _sum

    _sum = 0
    for i in range(100):
        _sum += rowData[i][i]
    if _sum > ans:
        ans = _sum

    _sum = 0
    for i in range(100):
        _sum += rowData[i][99 - i]
    if _sum > ans:
        ans = _sum

    print('#%d %d' % (testCase, ans))
