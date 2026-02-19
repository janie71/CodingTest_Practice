import sys
S=int(input())
sum=0
i=1
while S>sum:
    sum+=i
    i+=1

if S==sum:
    print(i-1)
else:
    # if S-(sum-i-(i-1))>i-1:
    print(i-2)