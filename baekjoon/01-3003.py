basiclist = [1, 1, 2, 2, 2, 8]
mylist = list(map(int, input().split()))
for i in range(0, 6):
    print(basiclist[i] - mylist[i], end=" ")