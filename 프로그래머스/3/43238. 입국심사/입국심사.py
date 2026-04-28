def solution(n, times):
    answer = 0
    high=n*times[0]
    low=times[0]

    while high>=low:
        Sum=0
        mid=(low+high)//2
        for i in times:
            Sum+=mid//i
        if Sum >= n:
            answer=mid
            high=mid-1
        else:
            low=mid+1
    
    return answer