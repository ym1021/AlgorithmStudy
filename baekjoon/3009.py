x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for j in range(3):
    if x_list.count(x_list[j])==1:
        x_res = x_list[j]
    if y_list.count(y_list[j])==1:
        y_res = y_list[j]
print(x_res, y_res)