def solution(brown, yellow):
    answer = []
    divisors=[]
    Sum=brown+yellow
    for h in range(1, Sum + 1):
        if Sum % h == 0:
            w=Sum//h
            if yellow == (w - 2) * (h - 2):
                answer=[w,h]    
                return answer
