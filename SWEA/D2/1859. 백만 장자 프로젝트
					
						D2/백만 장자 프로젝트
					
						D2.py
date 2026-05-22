# 5 12 11 8 2 6 3 9 1
#max값 측정
#max보다 작다->max-현재
#max보다 크다->max갱신

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc=int(input())
    List=list(map(int,input().split()))
    max=0
    cnt=0
    for i in range(tc-1,-1,-1):
        if max<List[i]:
            max=List[i]
        elif max>List[i]:
            cnt+=(max-List[i])
    print('#'+str(test_case)+' '+str(cnt))