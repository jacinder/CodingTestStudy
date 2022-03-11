def solution(s):
    length = []
    # 문자를 자르는 단위 slice_idx
    if(len(s) == 1):
        return 1
    
    for slice_idx in range(1, len(s)//2+1):
        # s를 끊어서 slice list만들기
        slice_list, stack = [], []
        for i in range(0, len(s), slice_idx):
            slice_list.append(s[i:i+slice_idx])
        slice_list.append('Z') # final character
        # print(slice_list)
        
        new_string = ""
        for item in slice_list:
            if len(stack) == 0:
                stack.append(item)
            elif stack[-1] == item:
                stack.append(item)
            else:
                new_string = new_string+f'{len(stack)}{stack[-1]}' if len(stack)>1 \
                else new_string+f'{stack[-1]}'
                stack = [item]
            # print(f'stack: {stack} new_string: {new_string}')
        length.append(len(new_string))
        
    answer = min(length)
    return answer
