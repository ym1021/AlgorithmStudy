
### <02 데이터 다루기 : 수와 텍스트, 비트>

# 여러 자료형
'''
iNum = 100000000000000000
print(iNum) # 정수

fNum = 0.123   # 8byte
print(fNum) # 실수 (부동 소수)

print(1<-2) # 불

_str = 'abc'
print(_str) # 문자열

a = 100+30j
print(type(a)) # 복소수 (실+허)
'''

# math 모듈
'''
import math
a = 100
b = 3

# 제곱
print(math.pow(a,b))    # 무조건 실수 타입 return
print(a**b)             # 알아서 return 타입 결정
# 제곱근
print(math.sqrt(2))
print(2**0.5)

ans = a/b   # 몫
print(ans)
ans = a%b
print(ans)  # 나머지
ans = a//b
print(ans)  # 정수화 몫
print(int(a/b)) # 정수화 몫 (더 빠름)
print(divmod(a,b))
# 튜플 ; 읽기 전용 (수정 불가)
'''

# 진수 타입 및 변환
'''
x02 = 0b100000
x08 = 0o40  # python 8진수 o 기호
x10 = 32
x16 = 0x20
print(x02, x08, x10, x16)
print(bin(x10))
print(oct(x10))
print(hex(x10))
'''

# 비트 연산
'''
# 11111111 -> 모든 비트가 1로 채워져 있으면 -1
a = 5   #00000101
b = 3   #00000011

print(a&b)
print(a|b)
print(a^b)
print(~b)
# >> : 2의 승으로 나눈 것과 같음
# << : 2의 승으로 곱한 것과 같음
'''
'''
# 비트 처리한 부분 집합
a = ['a','b','c']
n = 3
for i in range(1<<n):
    print('{', end=' ')
    for j in range(n):
        if i & (1<<j):
            print(a[j], end=" ")
    print('}')
'''


### <06 알고리즘>

# 1. 소수 검사 알고리즘 (약수)
'''
def isPrime(n):
    if n == 1:    return False

    _len = int(n**0.5)  # 정수부 검출

    for i in range(2, _len+1):
        if n%i == 0:    return False
    return True

a = 10007
if isPrime(a):    print('소수')
else:    print('비소수')

start = 100000000
end = 100010000

cnt = 0
for i in range(start, end+1):
    if isPrime(i):
        print(i)
        cnt += 1
print('cnt : ', cnt)
'''

# 2. 유클리드 알고리즘 (최대공약수)
'''
def gcd(p, q):
    if q==0:
        return p
    return gcd(q, p%q)

a = 105
b = 30
G = gcd(a,b)
L = a*b/G 
print('gcd :', G)
print('lcm :', L)
'''

a = 100000000001
if a%2 == 0:    print('짝수')
else:    print('홀수')

if a%2:    print('홀수')
else:    print('짝수')

if a&1 == 0:    print('짝수')
else:    print('홀수')

if a&1:    print('홀수')
else:    print('짝수')