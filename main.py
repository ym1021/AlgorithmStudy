# import sys
#
# sys.stdin = open('./files/input.txt','r')
# _str = input()
# cnt, *data = _str.split()
# print(cnt, data)
# idata = []
# for i in data:
#     idata.append(int(i))
#
# print(idata)
# iData = [range(1,11)]
# print(iData)
# iData = list(range(1,11))
# print(iData)
# data = list(map(int, _str.split()))
# print(data, type(data[0]))
#
# iData = list(map(int, input().split()))
# print(iData)
#
# a=100
# b=200
# print(a,b)
# for i in range(1,6):
#     print(i, end=" ")
# print()
# print('end')
# tc = 1
# ans = 100
# print('#%d %d'%(tc, ans))
# print('#{} {}'.format(tc, ans))
# arr1 = [0]*10
# arr1 = []
# print(arr1)
# for i in range(0,11):
#     arr1.append(i)
# print(arr1)
#
# arr1 = [i*2 for i in range(1,11)]
# print(arr1)
# arr2 = [[0]*5]*5
# print(arr2)
# arr2[0][0] = 100
# for i in range(0,5):
#     for j in range(0,5):
#         print(arr2[i][j], end=' ')
#     print()
# print(arr2)
# arr2 = list([0]*5 for _ in range(5))
# arr2 [0][0]= 100
# for i in arr2:
#     for j in i :
#         print(j,end = ' ')
# print(arr2)
# iNum = 1000000000000
# print(iNum)
# fNum = 0.123
# print(fNum)
# print(1<-2)
# _str = 'abc'
# print(type(_str))
#
# a = 100+30j
# print(type(a))
import math
# a = 100
# b = 3
# print(math.pow(a,b))
# print(a**b)
# print(math.sqrt(2))
# print(2**0.5)
# ans = a/b
# print(ans)
# ans = a%b
# print(ans)
# print(a//b)
# print(int(a/b))
# print(divmod(a,b))
#
# x02 = 0b100000
# x08 = 0o40
# x10 = 32
# x16 = 0x20
#
#
# print(x02, x08, x10, x16)
# print(bin(x10))
# print(hex(x10))
# print(oct(x10))
# a = 5 #0000101
# b = 3 #0000011
# print(a&b)
# print(a|b)
# print(a^b)
# print(~b)
#
# a = {'a','b','c'}
# n = 3
# for i in range(1<<n):
#     print('{', end = '')
#     for j in range(n):
#         if i & (1<<j):
#             print(a[j], end = " ")
#     print('}')
#
# def isPrime2(n):
#     if n == 1:
#         return  False
#루트를 취했을 떄 나오는 정수부분만 검열
    # _len = int(n**0.5)
    #
    # for i in range(2, _len+1):
    #     if n%i == 0:
    #         return False
    # return True
#
# a = 100000007
# if isPrime2(a):
#     print('소수')
# else:
#     print('소수가 아님')
# start = 100000000
# end = 100010000
#
# cnt = 0
# for i in range(start, end+1):
#     if isPrime2(i):
#         print(i)
#         cnt += 1
# print('cnt :', cnt)
# def gcd(p,q):
    # 나중에 정의 = pass
    # if q == 0:
    #     return p
    # return gcd(p, p%q)
#
# a = 105
# b = 30
# G = gcd(a, b)
# L = a*b/G
# print('gcd:',G)
# print('lcm :', b)

a = 1000000000001
if a&1:
    print('홀수')
else:
    print('짝수')