import sys
input = sys.stdin.readline

n = input()
arr = list(map(int, input().split()))
m = input()
check = list(map(int, input().split()))

dict = {}

for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for _ in check:
    if _ in dict:
        print(dict[_], end=' ')
    else:
        print(0, end=' ')

# https://hongcoding.tistory.com/12