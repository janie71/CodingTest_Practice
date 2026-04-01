import sys
from collections import deque

n=int(sys.stdin.readline())
pair=int(sys.stdin.readline())
visited=[0]*(n+1)
cnt=0
q=deque()

def bfs(graph, first,visited, cnt):
    q.append(first)
    visited[first]=1
    while q:
        c=q.popleft()
        for j in (graph[c]):
            if visited[j]==0:
                q.append(j)
                visited[j]=1
                cnt+=1
    print(cnt)
    
graph=[[] for _ in range(n+1)]
for i in range(pair):
    a,b=(list(map(int, sys.stdin.readline().split())))
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, visited, cnt)
