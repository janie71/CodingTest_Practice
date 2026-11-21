N=int(input())
sb_list=[]
for _ in range(N):
    sb_list.append(tuple(map(int, input().split())))

answer=10**9

def dfs(idx, curs,curb):
    global answer
    if idx==N:
        return

    s,b=sb_list[idx]
    # print(idx, abs((curs*s)-(curb+b)))
    answer=min(answer, abs((curs*s)-(curb+b)))
    dfs(idx+1, (curs*s), (curb+b))
    dfs(idx+1, curs, curb)


dfs(0, 1,0)
print(answer)