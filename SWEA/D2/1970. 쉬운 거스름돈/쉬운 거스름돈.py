'''
50,000 원
10,000 원
5,000 원
1,000 원
500 원
100 원
50 원
10 원
'''
T=int(input())
for testcase in range(1, T+1):
    N=int(input())
    answer=[0]*8

    if N>=50000:
        answer[0]=N//50000
        N=N-N//50000*50000
    if N >= 10000:
        answer[1] = N // 10000
        N = N - N // 10000 * 10000
    if N >= 5000:
        answer[2] = N // 5000
        N = N - N // 5000 * 5000
    if N >= 1000:
        answer[3] = N // 1000
        N = N - N // 1000 * 1000
    if N >= 500:
        answer[4] = N // 500
        N = N - N // 500 * 500
    if N >= 100:
        answer[5] = N // 100
        N = N - N // 100 * 100
    if N >= 50:
        answer[6] = N // 50
        N = N - N // 50 * 50
    if N >= 10:
        answer[7] = N // 10
        N = N - N // 10 * 10

    print(f'#{testcase}')
    print(*answer)