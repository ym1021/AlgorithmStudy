## 배열

# 상하좌우 4방향탐색
'''dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cx = 2
cy = 3
for i in range(0, 4):
    nx = cx + dx[i]
    ny = cy + dy[i]
    print('nx : ', nx, 'ny : ', ny)'''


### 검색

# 순차검색
'''data = [3,2,4,6,7,9,10,5,1]
key = 8
flag = False
cnt = 0
for i in data:
    cnt+=1
    if i == key:
        flag = True

if flag:
    print('Y')
else:
    print('N')
print('cnt : ', cnt)'''

# 이진검색
def selectSort(n):
    for i in range(n):
        maxIdx = 0
        for j in range(1, n-i):
            if data[maxIdx] < data[j]:
                maxIdx = j
        data[n-1-i], data[maxIdx] = data[maxIdx], data[n-1-i]

'''def mergeSort(start, end): # 오류 해결 필요
    if start < end:
        mid = int((start+end)/2)
        mergeSort(start, mid)
        mergeSort(mid+1, end)

        p = start
        q = mid+1
        idx = start
        while p<=mid or q<=end:
            if q > end or (p<=mid and data[p] < data[q]):
                temp[idx] = data[p]
                idx+=1
                p+=1
            else:
                temp[idx] = data[q]
                idx += 1
                p += 1
        for i in range(start, end+1):
            data[i] = temp[i]'''
def mergeSort(s, e):
    if s<e:
        m = int((s+e)/2)
        mergeSort(s, m)
        mergeSort(m+1, e)

        p = s
        q = m+1
        idx = s
        while p<=m or q<=e:
            if q>e or (p<=m and data[p] < data[q]):
                temp[idx] = data[p]
                idx+=1
                p+=1
            else:
                temp[idx] = data[q]
                idx += 1
                q += 1

        for i in range(s, e+1):
            data[i] = temp[i]


searchCnt = 0
# log2 N
def binarySearch(s, e, key):
    global searchCnt
    while s <= e:
        searchCnt+=1
        m = int((s+e)/2)
        if data[m] < key:
            s = m+1
        elif data[m] > key:
            e = m - 1
        else:
            return m
    return -1

def binarySearch2(s, e, key): # lis 알고리즘 구글링 필요
    while s <= e:
        m = int((s+e)/2)
        if data[m] < key:
            s = m+1
        elif data[m] > key:
            e = m - 1
        else:
            return m
    if data[s] < key:
        return s+1
    else:
        return s

n = 10
data = [1, 2, 11, 4, 3, 6, 5, 8, 7, 9, 10]
temp = [0]*len(data)
print('정렬 전 ', data)
# selectSort(n)
# mergeSort(0, n-1)
print('정렬 후 ', data)
'''
idx = binarySearch(0, n-1, 11)
print(idx)
print(searchCnt)
'''
key = 4
idx = binarySearch2(0, n-1, key)
print(idx)
