#최대증가수열(LIS)

def binarySearch(s, e, key):
    if dp[0] > key:
        return 0
    if dp[-1] < key:
        return len(dp)

    while s<=e:
        m = (s+e)//2
        if dp[m] == key:
            return m
        elif dp[m] < key:
            s = m+1
        else:
            e = m-1

    if dp[e] > key:
        return e
    else:
        return e+1

N = 100001
data = [2,1,5,7,9,4,5,6,8,10]
dp = []
path = {}#[0]*N
for i in data:
    if len(dp) == 0:
        dp.append(i)
        continue
    idx = binarySearch(0, len(dp)-1, i)

    if len(dp) == idx:
        dp.append(i)
    else:
        dp[idx] = i


    if idx == 0:
        path[i] = 0
    else:
        path[i] = dp[idx-1]

print(dp)
print(path)
last = dp[-1]
while last:
    print(last, end=' ')
    last = path[last]
print()
print('lis cnt :', len(dp))