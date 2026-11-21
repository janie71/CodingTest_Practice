n, m=map(int, input().split())
num_list=[i for i in range(1,n+1)]
answer=[]
def dfs(num_order):
    global answer
    if num_order and len(num_order)==m:
        print(' '.join(list(map(str, num_order))))
        return

    for i in num_list:
        if not num_order:
            num_order=[i]
        else:
            num_order.append(i)
        dfs(num_order)
        num_order.pop()
dfs([])