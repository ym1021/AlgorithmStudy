import sys
sys.stdin = open('../../files/input.txt', 'r')
tc = int(input())+1

for testCase in range(1, tc):
    num = int(input())
    # data = [i if i&1 else -i for i in range(1, num+1)] # 구글링 필요 : 리스트 컴프리헨션
    data = []
    for i in range(1, num+1):
        if i&1:
            data.append(i)
        else:
            data.append(-i)
    print('#%d %d' % (testCase, sum(data)))
