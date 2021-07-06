def solution(array, commands):
    
    answer = []
    
    for com in commands:
        array_ = array[com[0]-1:com[1]]
        array_.sort()
        answer.append(array_[com[2]-1])
    
    return answer