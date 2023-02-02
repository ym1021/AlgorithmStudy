from itertools import combinations

n, k = map(int, input().split())
key = tuple(map(int, input().split()))

combData = []
for i in combinations(list(range(1, n+1)), k):
    combData.append(i)
idx = combData.index(key)

if key == combData[-1]:
    print('NONE')
else:
    print(' '.join(map(str,combData[idx+1])))
