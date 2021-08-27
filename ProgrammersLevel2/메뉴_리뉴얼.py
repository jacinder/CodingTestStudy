from itertools import combinations 
import copy
def solution(orders, course):
    answers = []
    combination = {}

    for order in orders:
        for i in range(len(order)-1):
            combi = combinations(order, (i+2))
            for b in combi:
                c = list(b)
                c.sort()
                c = tuple(c)

                if c not in combination:
                    combination[c] = 1
                else: # 이미 combination이 있다면
                    combination[c] += 1

    for num in course:
        maximum=0
        maximum_key=[]
        for key,value in combination.items():
            if num == len(key):
                if value > maximum: # maximum이 업데이트
                    maximum = value
                    maximum_key = []
                    maximum_key.append(key)

                elif value == maximum: # maximum에 하나 더 추가
                    maximum_key.append(key)
        if maximum > 1:
            answers.extend(maximum_key)

    menu=[]

    for answer in answers:
        new_answer=""
        for element in answer:
            new_answer += element
        answer = new_answer
        menu.append(answer)


    menu.sort()


    return menu