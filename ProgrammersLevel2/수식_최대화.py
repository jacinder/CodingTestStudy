import re
import copy
import math
def solution(expression):
    expression = re.split('([-|+|*])', expression)
    max = 0

    # 3!의 케이스를 모두 만들어놓고, expression에 있는 연산문자가 있는 경우만 실행
    orders = ('+-*', '+*-', '-+*', '-*+', '*+-', '*-+')
    for order in orders:
        temp = copy.deepcopy(expression)
        for i in range(3):
            while order[i] in temp:
                idx = temp.index(order[i])
                temp[idx-1] = eval(f'{temp[idx-1]}{temp[idx]}{temp[idx+1]}')
                del(temp[idx+1])
                del(temp[idx])
                
        if abs(temp[0]) > max:
            max = abs(temp[0])
        
    return max