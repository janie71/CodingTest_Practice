import sys
from collections import deque

n=int(sys.stdin.readline())
List=[list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

visited=[[0] * n for _ in range(n)]
c1=0
c2=0
q=deque()
def bfs(l1, l2):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q.append((l1,l2))
    visited[l1][l2]=1
    while q:
        l1, l2=q.popleft()
        for i in range(4):
            nx=l1+dx[i]
            ny=l2+dy[i]
            if 0<=nx<n and 0<=ny<n and List[nx][ny] == List[l1][l2] and not visited[nx][ny]:
                visited[nx][ny] = 1 
                q.append((nx,ny))

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            c1+=1
           
#적록색약
for i in range(n):
    for j in range(n):
        if List[i][j]=='G':
            List[i][j]='R'

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            c2+=1
print(c1,c2)