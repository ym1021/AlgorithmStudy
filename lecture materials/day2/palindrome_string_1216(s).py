import sys
sys.stdin = open('../../files/input.txt', 'r')
T = 10
for _ in range(T):
    tc = int(input())
    a = [input() for _ in range(100)]
    b = [''.join(i) for i in zip(*a)]

    maxLen = 0
    chk = False
    for _len in range(100, 1, -1):
        for i in a:
            for j in range(100 - _len + 1):
                if i[j:_len + j] == i[_len-1 + j:j-1:-1]:
                    maxLen = _len
                    chk = True
                    break
            if chk:
                break
        if chk:
            break
    chk = False
    for _len in range(100, maxLen, -1):
        for i in b:
            for j in range(100-_len+1):
                if i[j:_len + j] == i[_len + j-1:j-1:-1]:
                    maxLen = _len
                    chk = True
                    break
            if chk:
                break
        if chk:
            break

    print('#%d %d' % (tc, maxLen))





