def solution(sizes):
    answer = 0
    for i in sizes:
        if(i[0] < i[1]):
            i[0],i[1] = i[1],i[0]
            
    max_w = max(i[0] for i in sizes)
    max_h= max(i[1] for i in sizes)
    answer = max_w * max_h
    return answer