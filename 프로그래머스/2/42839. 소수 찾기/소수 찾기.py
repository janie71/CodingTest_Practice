from itertools import permutations
def solution(numbers):
    answer = 0
    List=list(numbers)
    num_list=list(numbers)
    nums=set()
    for i in range(2,len(List)+1):
        num_list+=(permutations(List,i))
    for p in num_list:
        nums.add(int(''.join(p)))
    for num in nums:
        if num >1:        
            for i in range(2,int((num)**0.5)+1):
                if num%i==0:
                    break
            else:
                answer+=1
    
    return answer