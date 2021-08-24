import re
from operator import itemgetter

def solution(files):
     
    filename_sort = []
    answer = []
    
    for ori, filename in enumerate(files):
        n = re.search("\d", filename, flags=1)
        num_idx = n.start()
        head = filename[:num_idx]
        
        t = re.search("\D", filename[num_idx:], flags=1)
        if t is not None: # TAIL이 있는 경우
            tail_idx = t.start() + num_idx
            num = filename[num_idx:tail_idx]
            tail = filename[tail_idx:]
        else: # TAIL이 없는 경우
            num = filename[num_idx:]
            tail = None
        
        # print(f'HEAD:{head}, NUM:{num}, TAIL:{tail}')
        filename_sort.append([ori, head.lower(),int(num),tail])
        
#     print(files)
#     print(filename_sort)
    
    filename_sort.sort(key = itemgetter(1,2))
    for sorted in filename_sort:
        answer.append(files[sorted[0]])
        
    
    return answer