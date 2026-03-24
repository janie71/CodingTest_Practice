import sys
#idx는 n*m을 1차원으로 바꾼 배열
    #idx=지금 몇 번째 칸을 처리 중인지를 나타내는 1차원 인덱스
    #idx = row * M + col

def solve(idx):
    global count
    #끝까지 다 돌았을때
    if idx == n * m:
        count += 1
        return
    
    row = idx // m + 1
    column = idx % m + 1

    # 1. 넴모 안 놓는 경우
    solve(idx + 1)

    # 2. 넴모 놓는 경우 (2x2 체크)
    if not (graph[row-1][column] and graph[row][column-1] and graph[row-1][column-1]):
        graph[row][column] = 1 #넴모 놓기
        solve(idx + 1)
        graph[row][column] = 0 #넴모 복구

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
count = 0
solve(0)
print(count)