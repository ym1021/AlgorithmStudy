num = list(range(1, 10001))
remove = []
for i in num:
    for j in str(i):
        i += int(j)
    if i <= 10000:
        remove.append(i)
for rm in set(remove):
    num.remove(rm)
for _ in num:
    print(_)