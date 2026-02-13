def dfs(row):
    global res

    if row == N:
        res += 1
        return

    for col in range(N):
        if not visited[col] and not diag1[row + col] and not diag2[row - col + N - 1]:
            visited[col] = 1
            diag1[row + col] = 1
            diag2[row - col + N - 1] = 1

            dfs(row + 1)

            visited[col] = 0
            diag1[row + col] = 0
            diag2[row - col + N - 1] = 0


N = int(input())
res = 0

visited = [0] * N                  # 열
diag1 = [0] * (2*N)               # ↘ 대각선
diag2 = [0] * (2*N)               # ↗ 대각선

dfs(0)
print(res)