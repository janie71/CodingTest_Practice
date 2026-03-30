import sys
n=int(sys.stdin.readline())
prev_dp=[0,0,0]
cur_dp=[0,0,0]
for i in range(n):
    List=list(map(int, sys.stdin.readline().split()))
    cur_dp[0]=min(List[0]+prev_dp[1], List[0]+prev_dp[2])
    cur_dp[1]=min(List[1]+prev_dp[0], List[1]+prev_dp[2])
    cur_dp[2]=min(List[2]+prev_dp[0], List[2]+prev_dp[1])
    prev_dp=cur_dp
    cur_dp=[0,0,0]
print(min(prev_dp))