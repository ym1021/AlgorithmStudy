abc = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

num = 0
for _ in abc:
    for i in _:
        for j in word:
            if i == j:
                num += abc.index(_)+3
print(num)