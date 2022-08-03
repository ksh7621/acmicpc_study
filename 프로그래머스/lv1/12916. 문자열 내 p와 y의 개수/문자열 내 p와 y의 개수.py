def solution(s):
    answer = True
    cnt_p = 0
    cnt_y = 0
    for i in range(len(s)):
        if(s[i] == "p" or s[i] == 'P'):
            cnt_p += 1
        elif(s[i] == "y" or s[i] == 'Y'):
            cnt_y += 1
    
    if(cnt_p == cnt_y):
        return True
    elif(cnt_p == 0 and cnt_y == 0):
        return False
    else:
        return False
    

