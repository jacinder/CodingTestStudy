from itertools import combinations
def solution(orders, course):
    
    
    answerlist = []
    for cnt in course:
        flag = True
        temp = {}
        for order in orders:
            result = combinations(order, cnt)
            for menu in result:
                menu = ''.join(sorted(list(menu)))
                if menu in temp:
                    temp[menu] = temp[menu] + 1
                else:
                    temp[menu] = 1
        
        all_values = temp.values()
        # print(all_values)
        try:
            max_value = max(all_values)
        except ValueError as e:
            flag = False
            
        if max_value < 2:
            flag = False
            
        if flag:
            # print(f'temp: {temp}\nmax_value:{max_value}')
            for menu in temp:
                if temp[menu] == max_value:
                    # print(f'max_value를 가진 menu는 : {menu}-{temp[menu]}')
                    answerlist.append(menu)
            # print(f'update answer: {answerlist}')
        # else:
            # print(f'NO update answer: {answerlist}')
    
    answer = []
    for menu in answerlist:
        menu_ = ''.join(menu)
        answer.append(menu_)
    answer.sort()
    
    return answer
