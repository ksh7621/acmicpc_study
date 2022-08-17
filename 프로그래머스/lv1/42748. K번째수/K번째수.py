def solution(array, commands):
    answer = []   
    for m in range(len(commands)):
        temp = []
        temp = array
        i, j, k = map(int,commands[m])
        temp = temp[i-1:j]
        temp = sorted(temp) 
        answer.append(temp[k-1])
        print(temp)
        
    return answer