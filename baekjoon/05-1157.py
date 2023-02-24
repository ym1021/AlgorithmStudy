word = input().upper()
myword = list(set(word))
cnt = []
for i in myword:
   x = word.count(i)
   cnt.append(x)
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    cntmax = cnt.index(max(cnt))
    print(myword[cntmax])
