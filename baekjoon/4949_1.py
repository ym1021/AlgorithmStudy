while True:
  sen = input()
  if sen == ".":
    break
  for t in sen:
    stack = []
    if t == "(" or t == "[":
      stack.append(t)
    elif t == ")":
      if stack and stack[-1] == "(":
        stack.pop()
      else:
        stack.append(")")
        break
    elif t == "]":
      if stack and stack[-1] == "[":
        stack.pop()
      else:
        stack.append("]")
        break
    # print(stack)
  if stack:
    print("no")
  else:
    print("yes")