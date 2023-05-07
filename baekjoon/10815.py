import sys
input_ = sys.stdin.readline

n = int(input_())
sang = list(map(int, input_().split()))
m = int(input_())
arr = list(map(int, input_().split()))

sang.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

for _ in range(m):
    if binary_search(sang, arr[_], 0, n-1) is not None:
        print(1, end=" ")
    else:
        print(0, end=" ")

# sol2 : dictionary
# _dict = {}
# for i in range(len(cards)):
#     _dict[cards[i]] = 0  # 아무 숫자로 mapping
#
# for j in range(M):
#     if checks[j] not in _dict:
#         print(0, end=' ')
#     else:
#         print(1, end=' ')