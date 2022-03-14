DEBUG = False
from itertools import combinations_with_replacement
def solution(n, info):
    def scoring(apeach, ryan):
        if DEBUG:  print(f'[scoring] apeach:{apeach}, ryan:{ryan}')
        apeach_score, ryan_score = 0, 0
        for i, (a, r) in enumerate(zip(apeach, ryan)):
            if a == r == 0:
                continue
            if a >= r:
                apeach_score += (10 - i)
                if DEBUG:  print(f'apeach가 {10-i}점을 가져갑니다.') 
            else:
                ryan_score += (10 - i)
                if DEBUG:  print(f'ryan이 {10-i}점을 가져갑니다.')

        if DEBUG:  print(f'최종 apeach 점수는 {apeach_score}, ryan 점수는 {ryan_score}')
        
        return apeach_score, ryan_score
            
        
    def changeFormat(combination):
        result = [0]*11
        for item in combination:
            result[10-item] = result[10-item] + 1
        if DEBUG:  print(f'change format:{combination} -> {result}')
        return result
        
    
    win, max_score, max_case = False, -1, None
    for _case in list(combinations_with_replacement(range(0, 11), n)):
        case = changeFormat(_case)
        apeach_score, ryan_score = scoring(info, case)

        if ryan_score > apeach_score:
            win = True
            if (ryan_score - apeach_score) > max_score:
                max_score = ryan_score - apeach_score
                max_case = case
    
    # get answer
    answer = [-1]
    if win: answer = max_case
    
    return answer
