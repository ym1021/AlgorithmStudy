'''import sys
sys.stdin = open('../files/input.txt', 'r', encoding='utf-8')
tc = 11

for testCase in range(1, tc):
    _ = input()
    rowData = [input() for _ in range(100)]
    chk = True
    for _len in range(100, 1, -1):  # 문자열의 길이
        for words in rowData:  # 각각의 열의 문자열
            for i in range(100-_len+1):  # 경우의 수
                chk = True
                # for j in range(int(_len/2)):
                for j in range(int(_len // 2)):
                    if rowData[i+j] != rowData[100-i-j]:
                        chk = False
                        break
                if chk:
                    maxLen = _len
                    break
            if chk:
                break
        if chk:
            break

    print('#{} {}'.format(testCase, rowData[0]))'''

import sys
sys.stdin = open('../../files/input.txt', 'r')
T = 10
for _ in range(T):
    tc = int(input())
    rowData = [input() for _ in range(100)]

    colData = [''.join(x) for x in zip(*rowData)]

    maxLength = 0

    for mLen in range(100, 1, -1):
        for w in rowData:
            for i in range(100 - mLen + 1):
                chk = True
                for j in range(mLen // 2):
                    if w[i + j] != w[i + mLen - 1 - j]:
                        chk = False
                        break
                if chk:
                    break
            if chk:
                if maxLength < mLen:
                    maxLength = mLen
                break
    for mLen in range(100, maxLength, -1):
        for w in colData:
            for i in range(100 - mLen + 1):
                chk = True
                for j in range(mLen // 2):
                    if w[i + j] != w[i + mLen - 1 - j]:
                        chk = False
                        break
                if chk:
                    break
            if chk:
                if maxLength < mLen:
                    maxLength = mLen
                break

    print('#%d %d' % (tc, maxLength))

