num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    # print("num", num, "line", line)

if line % 2 == 0:
    son = num
    mom = line - num + 1
else:
    son = line - num + 1
    mom = num

print(son, '/', mom, sep="")


