def solution(s):
    answer = []
    s_list = list(s.split(" "))
    
    for i in range(len(s_list)):
        for j in range(len(s_list[i])):
            if j % 2 == 0:
                answer.append(s_list[i][j].upper())
            elif j % 2 == 1:
                answer.append(s_list[i][j].lower())            
        answer.append(" ")
    del answer[-1]
    ans = ''.join(answer)    
    return ans