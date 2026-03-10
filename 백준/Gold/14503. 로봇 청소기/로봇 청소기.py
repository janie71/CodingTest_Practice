import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 북, 동, 남, 서 (왼쪽 방향 전환을 위해 순서 설정)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 방문 처리 (청소한 곳은 2로 변경)
visited = [[0] * m for _ in range(n)]
visited[r][c] = 1
count = 1

while True:
    turned = 0
    for _ in range(4):
        # 1. 왼쪽으로 회전
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        # 2. 청소 안 된 공간이 있으면
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = 1
            count += 1
            r, c = nr, nc
            turned = 1
            break
    
    # 3. 네 방향 모두 청소할 곳이 없으면
    if turned == 0:
        # 후진 (바라보는 방향 유지)
        nr = r - dr[d]
        nc = c - dc[d]
        
        # 후진 가능한지 확인
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
            r, c = nr, nc
        else:
            print(count)
            break
