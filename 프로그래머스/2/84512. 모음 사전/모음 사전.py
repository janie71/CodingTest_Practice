def solution(word):
    # 각 자리별 가중치: 5번째=1, 4번째=6, 3번째=31, 2번째=156, 1번째=781
    weights = [781, 156, 31, 6, 1]
    vowels = "AEIOU"
    
    answer = 0
    for i, c in enumerate(word):
        # 해당 자리에서 c 이전 모음 개수 × 해당 자리 weight
        answer += vowels.index(c) * weights[i] + 1
    
    return answer