import math

def isdiv(a):
    div = []
    cnt = 0
    for i in range(1, int(math.sqrt(a))+1):        
        if a % i == 0:
            cnt += 2        
        else: continue        
        if(i**2 == a):
            cnt -= 1   
    return cnt          
    
    
def solution(left, right):
    answer = 0
    counter = 0
    even = 0
    odd = 0
    for i in range(left, right+1):
        counter = isdiv(i)
        print(counter)
        if(counter % 2 == 0):
            even += i
        else:
            odd += i
    answer = even-odd
    return answer