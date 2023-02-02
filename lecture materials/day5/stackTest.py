# stack : LIFO(last in first out), 항아리
# list 구조를 스택으로 사용해도 무방 하지만 삽입&삭제에 많은 시간 소요
# 스택 사용 : 계산기 구현

'''stack : LIFO(last in first out), 항아리
list 구조를 스택 으로 사용 무방
push => append==
pop  => pop
peek => stack[-1]
isFull => X
isEmpty'''

stack = []
stack.append(100)
stack.append(200)
print(stack)
print('pop :', stack.pop())
print(stack)
if len(stack):
    print('pop :', stack.pop())
    print(stack)
if stack:#len(stack):
    print('poppop')
    print('pop :', stack.pop())
    print(stack)

# DFS : 스택, BFS : 큐
