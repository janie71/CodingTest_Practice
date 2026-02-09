import sys
N=int(sys.stdin.readline())
pos=[]
neg=[]
zero=0
for i in range(N):
    a=int(sys.stdin.readline())
    if a>0:
        pos.append(a)
    elif a<0:
        neg.append(a)
    else:
        zero+=1
res=[]

#양수:큰것부터 곱하기&두수의 곱이 덧셈보다 작을 가능성
if pos:
    pos.sort()
    pos.reverse()
    if len(pos)%2==1:#음수
        L=len(pos)-1
        res.append(pos[-1])#제일 작은수는 그냥 더하기
    else:
        L=len(pos)
    for j in range(0, L, 2):
        if pos[j]*pos[j+1]>=pos[j]+pos[j+1]:
            res.append(pos[j]*pos[j+1])
        else:
            res.append(pos[j]+pos[j + 1])

#음수: 작은것부터 곱하기& 0이 존재하고 음수가 홀수개이면 연산x(제일 큰수와 0이랑 곱하기)
#0이 존재x, 음수 홀수개이면 그냥 더하기
if neg:
    neg.sort()
    if len(neg)%2==1:#음수
        L=len(neg)-1
        if zero==0:#0이 없다면
            res.append(neg[-1])
    else:
        L=len(neg)
    for j in range(0, L, 2):
        if neg[j]*neg[j+1]>=neg[j]+neg[j+1]:
            res.append(neg[j]*neg[j+1])
        else:
            res.append(neg[j]+neg[j + 1])
print(sum(res))