import sys
sys.stdin = open('../../files/input.txt', 'r')
for test_case in range(1, 11):
    n, data = input().split()
    stk = [0]
    stk.append(data[0])
    iLen = int(n)
    for i in range(1, iLen):
        if stk[-1] == data[i]:
            stk.pop()
        else:
            stk.append(data[i])
    print('#%d %s' % (test_case, ''.join(stk[1:])))
