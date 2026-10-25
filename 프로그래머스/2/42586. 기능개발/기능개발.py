def solution(progresses, speeds):
    answer = []
    result = []
    for order in range(len(progresses)):
        day=(100-progresses[order])//speeds[order]
        if (100-progresses[order])%speeds[order]:
            day+=1
        if not result or result[-1]<day:
            result.append(day)
            answer.append(1)
        elif result[-1]>=day:
            answer[-1]+=1
    return answer