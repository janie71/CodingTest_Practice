T=int(input())
for _ in range(1,T+1):
    N=int(input())
    answer=0

    num_list=[list(map(int,input().strip())) for i in range(N)]
    for n in range(0,N//2):
        answer+=sum(num_list[n][N//2-n:N//2+n+1])
    for n in range(N//2, N):
        answer+=sum(num_list[n][n-N//2:N-n+N//2])

    print(f'#{_} {answer}')