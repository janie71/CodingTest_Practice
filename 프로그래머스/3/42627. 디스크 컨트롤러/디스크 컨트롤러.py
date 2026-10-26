import heapq
def solution(jobs):
    len_jobs=len(jobs)
    heap=[]
    answer = 0
    time=0
    heapq.heapify(jobs)
    while jobs or heap:
        while jobs and jobs[0][0]<=time:
            s,l=heapq.heappop(jobs)
            heapq.heappush(heap, [l,s])
        if heap:
            l,s=heapq.heappop(heap)
            answer+=l+time-s
            time+=l
        else:
            time=jobs[0][0]
    return answer//len_jobs