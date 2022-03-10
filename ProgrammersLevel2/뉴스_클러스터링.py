def solution(str1, str2):
    # 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1
    strings = [list(str1.upper()), list(str2.upper())]
    lists = [[],[]]
    
    for idx, string in enumerate(strings):
        for i in range(len(string)-1):
            pair = string[i]+string[i+1]
            if pair.isalpha():
                lists[idx].append(pair)
    
    if len(lists[0]) == 0 and len(lists[1]) == 0:
        jaccard = 1
    
    else:
        common = []
        list2_copy = lists[1].copy()
        # get common items
        for item in lists[0]:
            if item in list2_copy:
                common.append(item)
                list2_copy.remove(item)
        intersection = len(common)
        union = len(lists[0])+len(lists[1])-len(common)
        jaccard = intersection / union
    
    answer = int(jaccard * 65536)
    return answer
