from itertools import combinations
def solution(numbers):
    answer = []
    num_list = list(combinations(numbers,2))
    for i in num_list:
        if sum(i) not in answer:
            answer.append(sum(i))
    answer = sorted(answer)
    return answer