import sys
T=int(input())
for _ in range(T):
    n=int(input())
    ct_d={}
    res=1
    for i in range(n):
        cn, ct=map(str, sys.stdin.readline().split())
        if ct in ct_d:
            ct_d[ct]+=1
        else:
            ct_d[ct]=1
    for value in ct_d.values():
        res*=value+1
    print(res-1)