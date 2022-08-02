def solution(n):
    answer = 0    
    n_list = list(map(int,str(n)))
    n_list = sorted(n_list, reverse = True)
    answer = "".join(map(str,n_list))
    return int(answer)