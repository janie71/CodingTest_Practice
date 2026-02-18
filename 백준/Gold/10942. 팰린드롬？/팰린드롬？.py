import sys
N=int(input()) #N=7
List=[0]+list(map(int, sys.stdin.readline().split()))
dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1): #범위 같으면 무조건 1
    dp[i][i]=1
for j in range(1,N): #범위 1차이, 1~6
    if List[j]==List[j+1]:
        dp[j][j+1]=1
        t1=j
        t2=j+1
        while dp[t1][t2]==1:
            if t1-1<1 or t2+1>N: #list범위(1~N) 초과하지 않는 내에서 진행
                break
            elif List[t1-1]==List[t2+1]:
                dp[t1-1][t2+1]=1
            t1 -= 1
            t2 += 1

for k in range(1, N-1): #범위 2차이, 1~5
    if List[k] == List[k + 2]:
        dp[k][k + 2] = 1
        t1=k
        t2=k+2
        while dp[t1][t2]==1:
            if t1-1<1 or t2+1>N: #list범위(1~N) 초과하지 않는 내에서 진행
                break
            elif List[t1-1]==List[t2+1]:
                dp[t1-1][t2+1]=1
            t1 -= 1
            t2 += 1

M=int(input())
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s][e])