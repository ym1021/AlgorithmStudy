'''
strData = ['aaa','bbb','ccc']
strData = [1,2,3,4,5,6,7,8,9]
#print('-'.join(['aaa','bbb']))
print(''.join(list(map(str,strData))))
'''
'''_str = '0123-4567-89012'
print(_str.rfind('-'))
ans = []
idx = 0
while 1:
    idx = _str.find('-', idx)
    if idx == -1:
        break
    ans.append(idx)
    idx+=1
print(ans)
'''
'''
idx = _str.find('-',5)
print(idx)'''
#print(_str.split('-'))
'''
idx = _str.find('10')
print(idx)'''
'''
print(len(_str))
print([_str])
print(list(_str))
print(_str[:2+1])#substr, subString
print(_str.count('02'))
idx = -1
if '1' in _str:
    idx = _str.index('1')
print(idx)'''

data = [(1,2,3),(1,2,4),(1,2,5)]
key = '1 2 3'
key = tuple(map(int, key.split()))
print(key)
idx = data.index(key)
print(idx)
if idx == len(data)-1:
    print('None')
else:
    print(' '.join(map(str,data[idx+1])))


