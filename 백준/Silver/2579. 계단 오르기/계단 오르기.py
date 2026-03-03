# 코드를 작성해주세요
import sys
n=int(input())
List=[int(sys.stdin.readline().strip()) for i in range(n)]
dp=[0]*n

if n==1:
    dp[0]=List[0]
    print(dp[0])
elif n==2:
    dp[0]=List[0]
    dp[1]=List[1]+dp[0]
    print(dp[1])
elif n==3:
    dp[0]=List[0]
    dp[1]=List[1]+dp[0]
    dp[2]=max(dp[0]+List[2], List[1]+List[2])
    print(dp[2])
else:
    dp[0]=List[0]
    dp[1]=List[1]+dp[0]
    dp[2]=max(dp[0]+List[2], List[1]+List[2])
    for j in range(3,n):
        dp[j]=max(dp[j-2]+List[j],dp[j-3]+List[j-1]+List[j])
        
    print(dp[-1])