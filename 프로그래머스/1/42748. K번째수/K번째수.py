def solution(array, commands):
    answer = []
    for command in commands:
        start, end, loc=command
        temp=(array[start-1:end])
        temp=sorted(temp)
        answer.append(temp[loc-1])
    return answer