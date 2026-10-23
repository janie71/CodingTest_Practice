def solution(nums):
    answer = 0
    n=len(nums)
    n2=n//2
    s=set(nums)
    sn=len(list(s))
    answer=min(sn,n2)
    return answer