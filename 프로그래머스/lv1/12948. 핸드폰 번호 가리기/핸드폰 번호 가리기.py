def solution(phone_number):
    answer = []
    pn_list = list(phone_number)
    for i in range(len(pn_list)-4):
        answer.append("*")
    for j in range(4, 0, -1):
        answer.append(pn_list[-j])
    b = ""
    return b.join(answer)