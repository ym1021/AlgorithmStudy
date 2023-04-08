# words = [input() for i in range(5)]
word = []
for _ in range(5):
    word.append(input())

for j in range(15):
    for i in range(5):
        if j < len(word[i]):
            print(word[i][j], end='')
