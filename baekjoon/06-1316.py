num = int(input())
res = num
for _ in range(num):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            res -= 1
            break
print(res)