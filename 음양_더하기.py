def solution(absolutes, signs):
    import numpy as np
    signs_ = [1 if sign == True else -1 for sign in signs]
    answer = int(sum(np.array(absolutes) * np.array(signs_)))
    
    return answer