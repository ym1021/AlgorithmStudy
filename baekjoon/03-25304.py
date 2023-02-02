# [print(('*'*n).center(9)) for n in [5,9,9,9,5]]
# [print(f'\x1b[{8-x};{x}H*')for x in [5,4,3]]
total = int(input())
num = int(input())
sum = 0
for i in range(0, num):
    mylist = list(map(int, input().split()))
    sum += mylist[0]*mylist[1]
if total == sum:
    print("Yes")
else:
    print("No")