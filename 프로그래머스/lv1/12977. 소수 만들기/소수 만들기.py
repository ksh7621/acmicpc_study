from itertools import combinations

def isprime(s1,s2,s3):
    total = s1+s2+s3
    for i in range(2,total):
        if(total % i == 0):
            return False      
    return True
    
def solution(nums):
    answer = 0
    L = list(combinations(nums,3))
    for i in L:
        if(isprime(i[0],i[1],i[2])):
            answer += 1
    return answer