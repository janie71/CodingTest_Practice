import itertools, sys

n,k=map(int, sys.stdin.readline().split())
nlist=list(map(int, sys.stdin.readline().split()))
clist=list(itertools.permutations(nlist,n))
res=0

#경우의 수마다 루프
for i in clist:
    templist=list(i)
    start=500
    temp=0
    #각 운동키트마다 루프
    for j in templist:
        if start-k+j>=500:
            start=start-k+j
            continue
        else:
            temp=1
            break
    if temp==0:
        res+=1
print(res)