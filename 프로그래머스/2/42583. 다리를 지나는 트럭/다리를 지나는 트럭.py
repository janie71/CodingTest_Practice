from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0 #시간계산
    d=deque([0]*bridge_length) #트럭이 해당 초에 안들어갔으면 0)

    #트럭단위로 for문 진행
    for i in truck_weights:
        c=0
        #1초 흘러서 트럭 이동
        d.popleft() #제일 앞에있던 트럭 다리 지나감
        answer+=1

        #현재 트럭을 넣을 수 있을때까지 deque에 있는 트럭빼기
        #while loop는 시간 단위(1초)
        while weight<i+sum(d):
            d.popleft()
            c+=1
        #0채워주기(트럭이 해당 초에 안들어갔으면 0)/while문 안돌았으면 c=0
        d.extend([0]*c)
        d.append(i)
        answer+=c
    #마지막 트럭이 다리 지날때까지 경과 시간 = bridge_length
    answer+=bridge_length
    return answer