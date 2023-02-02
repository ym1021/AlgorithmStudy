#연산자는 두개의 child
#피연산자는 반드시 단말
'''
N = 100+1
data = [0]*N
val=(op, num, leftC, rightC)
'''
def cal(root):
    if data[root][0]==0:
        return num

    a = cal(data[root][2])
    b = cal(data[root][3])
    if data[root][0] == '+':
        return a+b
    elif data[root][0] == '-':
        return a-b
    elif data[root][0] == '*':
        return a*b
    elif data[root][0] == '/':
        return a/b