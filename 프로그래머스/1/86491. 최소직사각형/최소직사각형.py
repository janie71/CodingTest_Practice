def solution(sizes):
    answer = 0
    max_w, max_h=0,0
    for w,h in sizes:
        if w<h:
            w,h=h,w
        if w>max_w:
            max_w=w
        if h>max_h:
            max_h=h    
    answer=max_w*max_h        
    return answer