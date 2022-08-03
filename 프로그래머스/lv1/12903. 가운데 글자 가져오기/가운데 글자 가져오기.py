def solution(s):
    answer = ''
    ll = len(s)
    if(ll % 2 == 0):
        answer = s[int(ll/2)-1]
        answer += s[int(ll/2)]
    else:
        answer = s[int(ll/2)]
            
        
    return answer