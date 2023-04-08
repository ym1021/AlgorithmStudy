# n, b = input().split()
# n = ''.join(reversed(n))
# b = int(b)
#
# arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# res = 0
#
# for _ in range(len(n)-1, -1, -1):
#     sum = arr.index(n[_])*(b**_)
#     res += sum
# print(res)

a, b = input().rstrip().split()
print(int(a, int(b)))