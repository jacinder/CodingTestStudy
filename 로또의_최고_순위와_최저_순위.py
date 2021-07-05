def solution(lottos, win_nums): 
    ranking = [6,6,5,4,3,2,1]
    zero_count = lottos.count(0)
    same_count = 0
    for i in lottos:  
        if i in win_nums:
            same_count += 1
            
    answer = [ranking[same_count+zero_count], ranking[same_count]]
    return answer