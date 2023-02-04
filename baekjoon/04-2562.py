num = []
for _ in range(0,9):
    _ = int(input())
    num.append(_)
# numbers = [int(input()) for _ in range(9)]

print(max(num))
print(num.index(max(num)) + 1)