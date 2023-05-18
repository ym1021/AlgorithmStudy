import sys
input_ = sys.stdin.readline

while True:
    ph = input_()
    stack = []

    if ph == ".":
        break;

    for i in ph:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(']')
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")