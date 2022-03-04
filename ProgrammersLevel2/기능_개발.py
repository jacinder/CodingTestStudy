import numpy as np
def solution(progresses, speeds):
    progresses = np.array(progresses)
    speeds = np.array(speeds)
    left_days = (100-progresses)/speeds
    left_days = np.ceil(left_days)
    # print(left_days)
    
    first, day, cnt = True, 0, 0
    answer = []
    for i,task in enumerate(left_days):
        if task > day:
            # print(f'현재 day: {day}, 현재 task: {task}')
            if first:
                # print(f'answer initialize: {answer}')
                first = False
            else: # 첫번째 원소가 아닐 경우 answer에 append
                answer.append(cnt)
                cnt = 0
                # print(f'answer update: {answer}')
            while task > day:
                day = day+1    
                # print(f'다음날: {day}')
        cnt = cnt+1
        # print(f'cnt update: {cnt}')
        
    answer.append(cnt)
    # print(f'answer update: {answer}')
    
    return answer
