import sys
N=int(input())
score_list=list(map(int, sys.stdin.readline().split()))
M=max(score_list)
sum=0
for i in score_list:
    sum+=i/M*100
print(sum/N)