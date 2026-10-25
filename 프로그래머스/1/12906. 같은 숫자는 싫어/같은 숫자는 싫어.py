def solution(arr):
    answer = []
    current=-1
    for num in arr:
        if current!=num:
            answer.append(num)
            current=num

    return answer