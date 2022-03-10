def solution(s):
    
    
    s = list(s)
    stack = []
    
    for item in s:
        if len(stack) > 0 and item == stack[-1]:
            # print(f'POP item: {item}, stack[-1]: {stack[-1]}')
            stack.pop()
        else:
            stack.append(item)
            # print(f'PUSH item: {item}, stack: {stack}')
    
    answer = 1 if len(stack) == 0 else 0
    
    return answer
