word = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for _ in cro:
    word = word.replace(_, 'i')
print(len(word))