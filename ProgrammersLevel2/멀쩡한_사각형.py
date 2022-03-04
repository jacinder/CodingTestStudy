from math import gcd
def solution(w,h):
    
    lined_space = 0 # 선이 그어진 면적
    g = gcd(w,h)
    
    if g == 1:
        lined_space = w+h-1
    else:
        lined_space = w+h-g
    
    answer = w*h - lined_space
    return answer
