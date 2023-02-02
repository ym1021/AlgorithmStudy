import sys
sys.stdin = open('../../files/input.txt', 'r')
tc = int(input())+1

def getNode(s1, s2):
    p1=[]
    while s1:
        p1.append(s1)
        s1 = p[s1]
    p2 = []
    while s2:
        p2.append(s2)
        s2 = p[s2]

    for i in p1:
        for j in p2:
            if i == j:
                return i
def getCnt(root):
    global resultCnt

    if root:
        resultCnt += 1
        getCnt(leftC[root])
        getCnt(rightC[root])

for testCase in range(1, tc):
    resultCnt = 0
    V, E, S1, S2 = map(int, input().split())
    leftC = [0]*(V+1)
    rightC = [0]*(V+1)
    p = [0]*(V+1)
    data = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        if leftC[data[i]]:
            rightC[data[i]] = data[i+1]
        else:
            leftC[data[i]] = data[i+1]
        p[data[i+1]] = data[i]

    commonNode = getNode(S1,S2)
#    getCnt(commonNode)
    stk = []
    stk.append(commonNode)
    while stk:
        u = stk.pop()
        resultCnt += 1
        if leftC[u]:
            stk.append(leftC[u])
        if rightC[u]:
            stk.append(rightC[u])
    print('#%d %d %d' % (testCase, commonNode, resultCnt))