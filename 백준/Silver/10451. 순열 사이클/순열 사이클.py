import sys
T=int(input())
for _ in range(T):
    N=int(input())
    List=[]
    per=list(map(int,sys.stdin.readline().split()))
    visited=[0]*N
    res=0
    for i in range(N):
        #visited=0이면 새로 넣기
        #넣고 per 값에 대해 루프
        #per값이 visited=1일때까지
        if visited[i]==0:
            # List.append([i+1,per[i]])
            res+=1
            visited[i]=1
            peri=per[i]
            while visited[peri-1]==0:
                #List[i+1].append([peri, per[peri]])
                visited[peri-1]=1
                peri=per[peri-1]
    print(res)