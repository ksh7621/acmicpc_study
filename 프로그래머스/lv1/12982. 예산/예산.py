def solution(d, budget):
    answer = 0
    d = sorted(d)
    
    for i in d:
        if budget < d[0]: break            
        budget -= i
        
        if(budget < 0): break
        elif budget == 0: 
            answer += 1
            break
        else:           
            answer += 1
    return answer