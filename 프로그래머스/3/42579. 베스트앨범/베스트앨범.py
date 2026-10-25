from collections import defaultdict
def solution(genres, plays):
    total=defaultdict(int)
    songs=defaultdict(list)
    answer = []
    for n in range(len(genres)):
        total[genres[n]]+=plays[n]
        songs[genres[n]].append((plays[n], n))
    genres_order=sorted(total, key=lambda x:total[x], reverse=True)
    
    for gen in genres_order:
        songs[gen].sort(key=lambda x:(-x[0],x[1]))
        for play, idx in songs[gen][:2]:
            answer.append(idx)
    return answer