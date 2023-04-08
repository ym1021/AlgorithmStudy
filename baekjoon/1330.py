mylist = list(map(int, input().split()))
if mylist[0]>mylist[1]:
    print(">")
elif mylist[0]<mylist[1]:
    print("<")
else:
    print("=")
