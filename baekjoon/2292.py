num = int(input())

bee = 1
cnt = 1

while num > bee:
    bee += cnt * 6
    cnt += 1
print(cnt)