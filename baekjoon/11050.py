import math

n, k = map(int, input().split())
print(math.factorial(k)//(math.factorial(n)*math.factorial(k-n)))
