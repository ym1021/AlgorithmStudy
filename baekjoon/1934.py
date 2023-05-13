import sys
input_ = sys.stdin.readline

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x, y):
    res = (x*y) // gcd(x, y)
    return res

t = int(input())

for _ in range(t):
    a, b = map(int, input_().rstrip().split())
    print(lcm(a, b))