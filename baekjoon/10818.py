num = int(input())
my = list(map(int, input().split()))

# min = my[0]
# max = my[0]
#
# for i in my[1:]:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# print(min, max)

print(min(my), max(my))
