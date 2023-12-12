def solution(targets):
    answer = 0
    bound = 0
    # sorted = O(NlogN)
    for s,e in sorted(targets):
        if bound > s:
            bound = min(bound,e)
        else:
            answer += 1
            bound = e
        
    
    return answer
