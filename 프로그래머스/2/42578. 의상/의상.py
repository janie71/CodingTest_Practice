def solution(clothes):
    dict={}
    for Name, Type in clothes:
        dict[Type]=dict.get(Type,0)+1
        
    answer=1
    for num in dict.values():
        answer*=num+1
    answer-=1
    return answer