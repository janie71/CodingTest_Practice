import sys
from collections import deque
T=int(input())

def bfs(n):
    q=deque()
    q.append(n)
    while q:
        a=q.popleft()
        visited[a] = 1
        if visited[Seq[a]]==0:
            q.append(Seq[a])

for i in range(T):
    count=0
    N=int(input())
    Seq=[0]+list(map(int,sys.stdin.readline().split()))
    visited = [0] * (N+1)
    for j in range(1,N+1):
        if visited[j]==0:
            bfs(j)
            count+=1
    print(count)