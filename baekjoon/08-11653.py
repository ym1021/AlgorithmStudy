num = int(input())

d = 2
while d <= num:
    if num % d == 0:
        print(d)
        num = num / d
    else:
        d += 1