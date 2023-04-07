arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, input().split())
res = ''

while n != 0:
    res += str(arr[n % b])
    n = n // b
print(res[::-1])