import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [[0] * M for _ in range(N)]
res = 0

def dfs(idx):
    global res

    # 모든 칸 다 본 경우
    if idx == N * M:
        res += 1
        return

    r = idx // M
    c = idx % M

    # 1. 현재 칸에 안 놓기
    dfs(idx + 1)

    # 2. 현재 칸에 놓기 (조건 체크)
    # 2×2 검사
    if r > 0 and c > 0:
        if board[r-1][c] and board[r][c-1] and board[r-1][c-1]:
            return  # 놓으면 2×2 완성 → 금지

    # 놓기
    board[r][c] = 1
    dfs(idx + 1)
    board[r][c] = 0  # 백트래킹

dfs(0)
print(res)