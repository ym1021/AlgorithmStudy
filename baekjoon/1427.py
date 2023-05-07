n = int(input())
arr = []

for i in str(n):
    arr.append(int(i))

arr.sort(reverse=True)

for _ in arr:
    print(_, end="")