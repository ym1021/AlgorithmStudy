import math

num = int(input())

for _ in range(num):
    n, k = map(int, input().split())
    print(math.factorial(k)//(math.factorial(n)*math.factorial(k-n)))
