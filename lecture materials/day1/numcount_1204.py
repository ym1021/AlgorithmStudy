import sys
sys.stdin = open('../../files/input.txt', 'r')
tc = int(input())+1

for testCase in range(1, tc):
    _ = input()
    nums = list(map(int, input().split()))
    # 모든값이 0으로 초기화된 배열 만들기
    cnts = [0]*101
    for i in nums:
        cnts[i] += 1
    # maxValue = max(cnts)
    # maxIdx = cnts.index(maxValue)
    # maxIdx = 0
    maxV = max(cnts)
    maxIdx = cnts.index(maxV)
    # for i in range(1, 101):
    for i in range(maxIdx, 101):
        # if(cnts[maxIdx] <= cnts[i]):
        if(cnts[maxIdx] == cnts[i]):
            maxIdx = i
    print('#{} {}'.format(testCase, maxIdx))
