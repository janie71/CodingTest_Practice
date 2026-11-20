N = int(input())
for i in range(1,N+1):
    num_list=list(map(int, str(i)))
    result=0
    for j in num_list:
        if j == 3 or j ==6 or j ==9:
            result+=1
    if not result:
        print(i, end = " ")
    else:
        print('-'*result, end = " ")