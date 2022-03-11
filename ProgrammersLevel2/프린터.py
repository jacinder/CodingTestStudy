from collections import deque
def solution(priorities, location):
    
    priorities_table = {i:prior for i,prior in enumerate(priorities)}
    orders = [i for i in range(len(priorities))]
    orders = deque(orders)

    answer = 0
    result = []
    

    while len(orders) > 0:
        prior_max = max(list(priorities_table.values()))
        idx = orders.popleft()
        prior_cur = priorities_table[idx]

        if prior_max > prior_cur:
            orders.append(idx)
        else:
            result.append(idx)
            del priorities_table[idx]
        
    
    answer = result.index(location) + 1
    
        
    
    return answer
