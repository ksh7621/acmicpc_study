def solution(s, n):
    answer = []
    s_list = list(s)
    for i in s_list:        
        if(ord(i) == 90):
            answer.append(chr(ord(i)-26 + n))
        elif(ord(i) == 122):
            answer.append(chr(ord(i)-26 + n))            
        elif(i == " "):
            answer.append(" ")
        elif(ord(i)>= 65 and ord(i) <= 90):
            if (ord(i) + n) > 90:
                answer.append(chr(ord(i)-26 + n))
            else:
                answer.append(chr(ord(i) + n)) 
        elif(ord(i)>= 97 and ord(i) <= 122):
            if (ord(i) + n) > 122:
                answer.append(chr(ord(i)-26 + n))
            else:
                answer.append(chr(ord(i) + n))       
        else:
            answer.append(chr(ord(i) + n))        
    return ''.join(answer)