### 2차원 정렬
# 원본 데이터를 정렬해도 될 경우 sort
'''
data = [2, 3, 4, 1, 5, 6, 8, 7, 9, 10]

print('정렬 전 :', data)
# default sort : ascending(오름차순)
data.sort()  # 옵션 : keys, reverse
data.sort(reverse=True)
data2 = sorted(data)
print('정렬 후 :', data)
print('정렬 후 :', data2)
'''

# 원본 데이터를 정렬하면 안되는 경우 sorted
'''
def cmp(a):
    return a[1]

data = [[2, 1],[1, 3],[1, 2]]
# 1 : asc, 2 : asc
print(sorted(data))
# 2 : asc
# print(sorted(data, key=lambda x:x[1])) # 람다(익명함수) 사용
print(sorted(data, key=cmp))
# 1 : asc, 2 : desc
print(sorted(data, key=lambda x:(x[0], -x[1])))
'''

# counting sort : 정수 (0<+), 가장 큰 숫자를 기반으로 배열 크기 설정
data = [1, 4, 2, 3, 5, 6, 7, 8, 9, 88, 100]
maxV = max(data)
cntArr = [0]*(maxV+1)
for i in data:
    cntArr[i]+=1

print("[", end=' ')
for i in range(0, maxV+1):
    if cntArr[i]:
        for j in range(cntArr[1]):
            print(i, end=' ')

print()

### 데이터 주소값
# data = [1, 2, 3, 4, 5]
# data2 = data  # 주소값 동일
# data3 = [1, 2, 3, 4, 5]
# print('1:2', data == data2, id(data), id(data2))
# print('1:3', data == data3, id(data), id(data3))

data = [1, 2, 3, 4, 5]
data2 = data.copy()  # 주소값 달라짐
print('1:2', data == data2, id(data), id(data2))
data2[0] = 100
print(data[0])
print(data2[0])

data1 = [[1, 2],[3, 4],[5, 6]]
'''
data2 = data1.copy()
print(data1)
print(data2)
print(id(data1), id(data2))
'''
data2 = sorted(data1)
data2[0][0] = 200
print(data1)
print(data2)
