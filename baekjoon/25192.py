n = int(input())
dict = {}
cnt = 0

for _ in range(n):
    chat = input()
    if chat == "ENTER":
        for key, value in dict.items():
            if value == 1:
                cnt += 1
        dict = {}
    else:
        if chat not in dict:
            dict[chat] = 1

for key, value in dict.items():
    if value == 1:
        cnt += 1

print(cnt)