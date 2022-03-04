import re
def solution(records):
    # print(records)
    uid_uname = {}
    temp = []
    answer = []
    
    
    for record in records:
        if re.match('Enter', record):
            _,uid,uname = record.split()
            uid_uname[uid] = uname
            temp.append(f'{uid} 님이 들어왔습니다.')
            # print(f'{uid} {uname} 들어옴')
            
        elif re.match('Leave', record):
            _,uid = record.split()
            temp.append(f'{uid} 님이 나갔습니다.')
            # print(f'{uid} {uid_uname[uid]} 나감')
        
        else:
            _,uid,uname = record.split()
            # print(f'{uid} {uid_uname[uid]}에서 {uname}으로 바꿈')
            uid_uname[uid] = uname  # uid_uname 수정
            
        
    # print(uid_uname)
    
    
    for line in temp:
        uid,tmp1,tmp2 = line.split()
        answer.append(f'{uid_uname[uid]}{tmp1} {tmp2}')
    
    # print(temp)
    # print(answer)
    
    return answer
