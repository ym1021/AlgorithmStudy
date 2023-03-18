gra = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
sco = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
res = 0

for _ in range(20):
    sub, num, grade = input().split()
    num = float(num)
    if grade != 'P':
        total += num
        res += num * sco[gra.index(grade)]
print('%.6f'%(res/total))

