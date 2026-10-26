import heapq
def solution(operations):
    min_heap=[]
    max_heap=[]
    deleted=[False]*len(operations)
    
    for i,operation in enumerate(operations):
        op, num=operation.split(" ")
        num=int(num)
        if op=="I":
            heapq.heappush(min_heap,(num,i))
            heapq.heappush(max_heap,(-num,i))
        elif operation == "D 1":
            while max_heap and deleted[max_heap[0][1]]:
                heapq.heappop(max_heap)

            if max_heap:
                num, idx = heapq.heappop(max_heap)
                deleted[idx] = True

        elif operation == "D -1":
            while min_heap and deleted[min_heap[0][1]]:
                heapq.heappop(min_heap)

            if min_heap:
                num, idx = heapq.heappop(min_heap)
                deleted[idx] = True
    
    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap) 
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)
    if not min_heap:
        return [0,0]
    return [-max_heap[0][0],min_heap[0][0]]