a,b,c = map(int, input().split())
total = 0
if a==b==c:
    total=10000+(a*1000)
elif a==b or a==c:
    total=1000+(a*100)
elif b==c:
    total=1000+(b*100)
else:
    if a>b and a>c:
        total=a*100
    elif b>a and b>c:
        total=b*100
    else:
        total=c*100
print(total)
