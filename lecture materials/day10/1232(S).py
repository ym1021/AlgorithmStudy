import sys
sys.stdin = open('../../files/input.txt', 'r')

def cal(root):
    if data[root][0] == 0:
        return data[root][1]
    a = cal(data[root][2])
    b = cal(data[root][3])
    if data[root][0] == '+':
        return a + b
    if data[root][0] == '-':
        return a - b
    if data[root][0] == '*':
        return a * b
    if data[root][0] == '/':
        return a / b

tc = 11
for testCase in range(1, tc):
    N = int(input())
    data = [0]*(N+1)
    #op,num,leftC, rightC
    for i in range(N):
        _list = input().split()
        if _list[1][0] < '0':
            data[int(_list[0])] = [_list[1], 0, int(_list[2]), int(_list[3])]
        else:
            data[int(_list[0])] = [0, int(_list[1])]
    print('#%d %d' % (testCase, int(cal(1))))