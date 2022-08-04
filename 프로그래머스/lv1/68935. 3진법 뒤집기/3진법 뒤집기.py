def solution(n):
    answer = 0
    th = []
    
    for i in range(n):
        if (n//3 == 0):
            rem = n % 3
            th.append(rem)
            break
        else:
            rem = n % 3
            n = n//3
            th.append(rem)    
            
    th = th[::-1]
    
    for j in range(len(th)):
        answer += (3**j*th[j])
        
    return answer