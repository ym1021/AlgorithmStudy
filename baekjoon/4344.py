_ = int(input())
for _ in range(_):
    num = list(map(int, input().split()))
    avg = (sum(num)-num[0])/num[0] # sum(num[1:])/num[0]
    cnt = 0
    for i in num[1:]:
        if i > avg:
            cnt += 1
    per = cnt/num[0]*100
    print("%.3f"%per+"%")