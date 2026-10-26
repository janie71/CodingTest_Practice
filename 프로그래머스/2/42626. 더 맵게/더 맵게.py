import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville)>=2:
        low1=heapq.heappop(scoville)
        low2=heapq.heappop(scoville)
        if low2==0:
            return -1
        if low1>=K:
            return answer
        heapq.heappush(scoville, low1+low2*2)
        answer+=1
    if len(scoville)==1 and heapq.heappop(scoville)>=K:
        return answer

    return -1