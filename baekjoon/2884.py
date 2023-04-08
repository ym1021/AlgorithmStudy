mylist = list(map(int, input().split()))

min = mylist[1] - 45
hour = mylist[0]
if min < 0:
    hour = hour - 1
    min = min + 60
    if hour < 0:
        hour = hour + 24
print(str(hour)+" "+str(min))