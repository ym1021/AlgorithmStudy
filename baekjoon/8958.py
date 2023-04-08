num = int(input())
for _ in range(num):
    ox = list(input())
    score = 0
    total = 0
    for i in ox:
        if i == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)
