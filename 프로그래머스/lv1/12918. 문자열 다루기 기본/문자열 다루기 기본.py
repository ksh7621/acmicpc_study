def solution(s):
    answer = True
    ll = len(s)
    for i in range(ll):
        if(ll == 4 or ll == 6):
            if s[i].isdigit():
                answer = True
            else:
                answer = False
                break
        else:
            answer = False
            break
    return answer