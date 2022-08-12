def solution(N, stages):
    answer = []
    user = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)  
        
        if user == 0:
            fail = 0
        else:
            fail = count/user
            
        answer.append((i,fail))
        user -= count
        
    answer = sorted(answer, key = lambda x: (-x[1],x[0]))
    
    answer = [i[0] for i in answer]
        
    return answer