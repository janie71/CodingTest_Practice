import sys
H,W=map(int,sys.stdin.readline().split())
List=list(map(int,sys.stdin.readline().split()))

start=-1
max=0
end=0
res=0
while end<W-1:
    for i in range(end, W-1):
        if List[i]>List[i+1]:
            start=i
            break
    if start==-1:
        break
    for j in range(start,W-1):
        #start보다 크거나 같은 값의 위치=end
        if List[j]<List[j+1] and List[start]<=List[j+1]:
            end=j+1
            break
        # start보다 작은것중 가장 큰 값의 위치 찾기
        elif List[j]<List[j+1]:
            if max==0 or List[max]<List[j+1]:
                max=j+1
    if end<=start and max==0:
        break
    elif end<=start:
        end=max

    for k in range(start+1,end):
        if min(List[start],List[end])>List[k]:
            res+=min(List[start],List[end])-List[k]
    max=0
    start=-1

print(res)