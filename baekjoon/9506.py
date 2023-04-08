while True:
    mylist = []
    num = int(input())
    if num == -1:
        break
    for i in range(1, num):
        if num % i == 0:
            mylist.append(i)
    if sum(mylist) == num:
        print(num, " = ", " + ".join(str(_) for _ in mylist), sep="")
    else:
        print(num, "is NOT perfect.")
