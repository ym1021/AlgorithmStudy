# 정올 1092 제곱수 출력 (분할정복)

mod = 20091024
x, y = map(int, input().split())
x %= mod

ans = 1
while y:
    if y & 1:  # 홀수 짝수 확인
        ans = ans * x
    x = (x*x)%mod
    y = y >> 1 # 시프트 연산

print(ans)
