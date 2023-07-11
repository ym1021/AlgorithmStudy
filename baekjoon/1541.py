arr = input().split('-')
s = 0
for _ in arr[0].split('+'):
    s += int(_)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)