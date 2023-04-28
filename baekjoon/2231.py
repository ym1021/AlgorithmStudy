num = int(input())

for i in range(1, num+1):
    n = sum((map(int, str(i))))
    n += i
    if num == n:
        print(i)
        break
    elif num == i:
        print(0)