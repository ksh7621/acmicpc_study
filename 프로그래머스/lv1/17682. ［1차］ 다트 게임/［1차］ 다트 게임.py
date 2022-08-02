def solution(dartResult):
    dartResult = dartResult.replace("10","A")
    print(dartResult)
    res = list(dartResult)
    print(res)
    stack = []   
    
    for i in range(len(res)):
        if res[i].isdigit() or res[i] == 'A':
            if(res[i] == 'A'):
                stack.append(10)
            else:
                stack.append(int(res[i]))
        elif res[i] == 'S':
            num = stack.pop()
            stack.append(num ** 1)
        elif res[i] == 'D':
            num = stack.pop()
            stack.append(num ** 2)
        elif res[i] == 'T':
            num = stack.pop()
            stack.append(num ** 3)
        elif res[i] == '*':
            num = stack.pop()
            if(len(stack)):
                stack[-1] *= 2
            stack.append(2*num)
        elif res[i] == '#':
            stack[-1] *= -1          
    
    return sum(stack)