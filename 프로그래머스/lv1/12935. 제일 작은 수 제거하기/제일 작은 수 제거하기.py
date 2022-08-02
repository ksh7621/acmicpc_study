import numpy as np

def solution(arr):
    answer = []
    np_arr = np.array(arr)       
    mini = np.min(np_arr) 
    
    for i in range(len(np_arr)):
        if np_arr[i] == mini: 
            continue
        else:
            answer.append(int(np_arr[i]))
            
    if len(answer) == 0:
        answer.append(int(-1)) 
  

    return answer