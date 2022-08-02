def solution(x):
    answer = True
    x = str(x)    
    x_li = list(x)    
    x_lli = []

    for i in range(len(x_li)):
        x_lli.append(int(x_li[i]))

    s = sum(x_lli)
    x = int(x)

    if x % s == 0:
        answer = True
    else:
        answer = False
    return answer