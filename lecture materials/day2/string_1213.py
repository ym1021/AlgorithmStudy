# trie : suffix array를 이용, 모든 부분 문자열을 구한 뒤 자동 정렬

import sys
sys.stdin = open('../../files/input.txt', 'r', encoding='utf-8')
tc = 11

for testCase in range(1, tc):
    '''_ = input()  # 테스트케이스 번호
    key = input()
    _str = input()

    sum = 0

    idx = -1
    while True:
        idx = _str.find(key, idx + 1)
        if idx == -1:
            break
        sum += 1

    print('#{} {}'.format(testCase, sum))'''

    input()  # 테스트케이스 번호
    key = input()
    _str = input()

    print('#{} {}'.format(testCase, _str.count(key)))
