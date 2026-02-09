import sys

num = 0
a=int(sys.stdin.readline())
stack=[]
result=[]

for i in range(a):
    b= sys.stdin.readline().strip()
    if b == "pop":
        if len(stack)==0:
            result.append(-1)
        else:
            result.append(stack[(len(stack))-1])
            stack.pop()
    elif b == 'size':
        result.append(len(stack))
    elif b == 'empty':
        if len(stack)==0:
            result.append(1)
        else:
            result.append(0)
    elif b=='top':
        if len(stack)==0:
            result.append(-1)
        else:
            result.append(stack[(len(stack)) - 1])
    else:
        num=b.split()
        stack.append(int(num[1]))
for i in range(len(result)):
    print(result[i])