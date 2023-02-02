import sys
sys.stdin = open('../../files/input.txt', 'r')

maxN = int(1e5)
nums = [0]*maxN
primes = []
#에라토스테네스체
for i in range(2, maxN):
    if nums[i]:
        continue
    primes.append(i)
    for j in range(i, maxN, i):
        nums[j] = 1

T = int(input())+1
for testCase in range(1, T):
    N, K = map(int, input().split())
    ans = 1
    for i in primes:
        if N<i:
            break
        cnt = 1
        tmp = int(N/i) # N//i
        while tmp:
            cnt+=tmp
            tmp//=i
        tmp = int((N-K) / i)
        while tmp:
            cnt -= tmp
            tmp//=i
        tmp = int(K / i)
        while tmp:
            cnt -= tmp
            tmp //= i
        ans = (ans*cnt)%1000000007

    print('#%d %d' % (testCase, ans))