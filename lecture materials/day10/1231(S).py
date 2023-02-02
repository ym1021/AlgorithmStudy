import sys
sys.stdin = open('../../files/input.txt', 'r')
tc = 11
def inOrder(root):
    if data[root]:
        inOrder(root*2)
        print(data[root], end='')
        inOrder(root*2+1)

for testCase in range(1, tc):
    N = int(input())
    data = [0]*((N+1)*2)
    for i in range(N):
        _list = input().split()
        data[int(_list[0])] = _list[1]
    print('#%d' % testCase, end=' ')
    inOrder(1)
    print()