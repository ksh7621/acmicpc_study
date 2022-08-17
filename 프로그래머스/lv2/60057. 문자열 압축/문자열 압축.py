def solution(s):
    answer = 0
    length = []
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)+1):
        string = ''
        count = 1
        temp = s[:i]        
        for j in range(i,len(s)+i,i):
            if temp == s[j:j+i]:
                count+=1
            else:
                if count != 1:
                    string = string + (str(count)) + temp
                else:
                    string = string + temp
                temp = s[j:j+i]
                count = 1
        length.append(len(string))
            
    return min(length)