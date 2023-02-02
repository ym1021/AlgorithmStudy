# import sys
# sys.stdin = open('./files/input.txt','r')
# for testCase in range(1,11):
#     cnt = int(input())
#     data = list(map(int, input().split()))
#     data.sort()
#
#     for i in range(0, cnt):
#         data[data.index(max(data))] -= 1
#         data[data.index(min(data))] += 1
#         cnt -= 1
#     ans = 0
#     print('#%d %d' %(testCase, max(data) - min(data)))
import sys
sys.stdin = open('../../files/input.txt', 'r')
tc = 11
for testCase in range(1, tc):
    dumpCnt = int(input())
    # map도 하나의 객체 그 객체가 갖고 있는 모든 요소를 리스트로 만드는 것. .
    dumpData = list(map(int, input().split()))
    dumpData.sort()
    while dumpCnt:
        dumpData[-1] -= 1
        dumpData[0] += 1
        dumpData.sort()
        dumpCnt -= 1
    print('#{} {}'.format(tc, max(dumpData)-min(dumpData)))
