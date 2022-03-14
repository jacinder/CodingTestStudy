from itertools import permutations
def solution(expression):
    
    operator = ['+', '-', '*']
    
    # 주어진 expression을 연산자 단위로 잘라서 list화하기
    temp = []
    expression_list = []
    for x in expression:
        if x in operator:
            expression_list.append(''.join(temp))
            expression_list.append(x)
            temp = []
        else:
            temp.append(x)
        
    if len(temp) != 0:
        expression_list.append(''.join(temp))
        temp = []
    
    prize = []
    for case in list(permutations(operator, 3)):
        # 후위표기법으로 바꾸고
        # print(f'우선순위: {case}')
        stack = []
        postfix = []
        
        for item in expression_list:
            if item in operator:
                priority = case.index(item)
                if len(stack)==0 or max(stack) < priority:
                    stack.append(priority)
                else: # stack에 원소가 있는데 나보다 우선순위가 높거나 같은 애가 있으면 작아질때까지 pop
                    while True:
                        pop = stack.pop()
                        postfix.append(case[pop])
                        if len(stack)==0 or max(stack) < priority:
                            break
                    stack.append(priority)
            else:
                postfix.append(item)
        
        while len(stack) != 0:
            pop = stack.pop()
            postfix.append(case[pop])
        
        # print(postfix)
                  
        # 후위표기법 연산하기
        stack = []
        for item in postfix:
            if item in operator:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(eval(f'{op1}{item}{op2}'))
            else:
                stack.append(item)
            # print(stack)
        
        prize.append(abs(stack[0]))
    
    
    answer = max(prize)
    return answer
