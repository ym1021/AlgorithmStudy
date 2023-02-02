
### <01 표준 입출력>

# 파일 입출력
'''
import sys
sys.stdin = open('../files/input.txt', 'r', encoding='UTF-8') # 주석 처리 후 제출
_str = input()  # 해당 파일에 표준 입력 받음
cnt, *data = _str.split()
print(cnt, data)
'''


# 문자 -> 정수 타입 변환 (map 함수)
''' 옳 X
idata = []
for i in data:
    idata.append(int(i))
print(idata)

idata = [range(1,11)]
idata = list(range(1,11))   # 범위 내 연속 값 저장
print(idata)
'''
''' 옳 O
data = list(map(int, _str.split()))
print(data, type(data[0]))
'''
''' 옳 O
iData = list(map(int, input().split()))
print(iData)
'''

# 간격 설정 및 개행
'''
a = 100
b = 200
print(a, b)
for i in range(1, 6):
    print(i, end=" ")
print()
print('end')
'''

# tc / ans 출력
'''
tc = 1
ans = 100
print('#%d %d' %(tc,ans))
print('#{} {}'.format(tc,ans))
'''

# 리스트 컴프리헨션 (수행시간 감소)
''' 옳 X
arr1 = [0]*10
arr1 = []
for i in range(0, 11):
    arr1.append(i)
print(arr1)
'''
''' 옳 O
arr1 = [i*2 for i in range(1,11)]
print(arr1)
'''

# 이차원 배열 생성
''' 옳 X
# 외관상 2차원 배열이나, 사실상 서로 동일한 메모리 참조
arr2 = [[0]*5]*5
print(arr2)
arr2[0][0] = 100
for i in range(0,5):
    for j in range(0,5):
        print(arr2[i][j], end=' ')
    print()
'''
''' 옳 O
# 단순 반복
arr2 = [list(0 for _ in range(5))]
# 리스트 참조가 아닌 복사
arr2 = [[0]*5 for _ in range(5)]
arr2[0][0] = 100
for i in arr2:
    for j in i:
        print(j, end=' ')
    print()
'''