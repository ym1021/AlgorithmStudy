cnt = 0
n = int(input())
num = n
while True:
    if num < 10:
        ten = 0
    else:
        ten = num // 10
    one = num % 10
    add = one + ten
    cnt = cnt + 1
    sum = (one*10)+(add%10)
    # print("sum = "+str(sum))
    if sum == n:
        print(cnt)
        break
    num = sum
