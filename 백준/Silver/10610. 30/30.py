N=list(map(int, list(input().strip())))

if(sum(N)%3!=0 or 0 not in N):
    print(-1)
    exit(0)
N.sort(reverse=True)
print(''.join(list(map(str,N))))