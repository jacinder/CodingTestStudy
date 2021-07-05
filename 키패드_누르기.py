def solution(numbers, hand):
    
    hand_ = {'right':'R', 'left':'L'}
    hand = hand_[hand]
    
    left = [1,4,7]
    right = [3,6,9]
    
    answer = ''
    lcurr = 11  # 임의로 *은 11, #은 12이라고 표현한다.
    rcurr = 12
    position = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        11:(3,0), 0:(3,1), 12:(3,2),
    }
    
    
    for n in numbers:
        if n in left:
            answer += 'L'
            lcurr = n
            
        elif n in right:
            answer += 'R'
            rcurr = n 
            
        else:
            # calculate ldist and rdist
            ldist = abs(position[lcurr][0]-position[n][0]) + abs(position[lcurr][1]-position[n][1])
            rdist = abs(position[rcurr][0]-position[n][0]) + abs(position[rcurr][1]-position[n][1])
            if ldist == rdist:
                answer += hand
                if hand == 'L':
                    lcurr = n
                else:
                    rcurr = n
            
            elif ldist < rdist:
                answer += 'L'
                lcurr = n
                
            else:
                answer += 'R'
                rcurr = n
            
    return answer