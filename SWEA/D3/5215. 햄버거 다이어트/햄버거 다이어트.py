T=int(input())

for testcase in range(1, T+1):
    N, L= map(int, input().split())
    ham = [tuple(map(int, input().split())) for _ in range(N)]
    answer=0

    def dfs(idx, total_score, total_kcal):
        global answer

        if idx == N:
            answer=max(answer, total_score)
            return
        score, kcal = ham[idx]

        if L>=total_kcal+kcal:
            dfs(idx+1, total_score+score, total_kcal+kcal)

        dfs(idx+1, total_score, total_kcal)

    dfs(0,0,0)
    print(f'#{testcase} {answer}')