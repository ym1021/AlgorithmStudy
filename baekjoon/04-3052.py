num = []
for i in range(0,10):
    i = int(input())
    num.append(i%42)
num = set(num)
print(len(num))
