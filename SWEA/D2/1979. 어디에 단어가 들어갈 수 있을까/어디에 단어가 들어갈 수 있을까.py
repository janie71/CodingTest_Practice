def wcount(word_list,K):

    result=0
    #가로
    for row in word_list:
        num=(''.join(list(map(str, row))))
        numlist=num.split('0')

        for i in numlist:
            if i=='1'*K:
                result+=1
    #세로
    for i in range(len(word_list)):
        col=[j[i] for j in word_list]
        num = (''.join(list(map(str, col))))
        numlist = num.split('0')

        for i in numlist:
            if i == '1' * K:
                result += 1
    return result

T = int(input())

for test_case in range(1, T + 1):
    N,K = map(int, input().split())
    word_list=[list(map(int, input().split())) for i in range(N)]

    print(f'#{test_case} {wcount(word_list,K)}')