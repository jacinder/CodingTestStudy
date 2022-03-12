def solution(s):
    def isCorrectBracket(s):
        bracket_idx = {'[':-1, ']':1, '(':-2, ')':2, '{':-3, '}':3}
        stack = []
        for c in s:
            
            # opening bracket
            if bracket_idx[c] < 0: 
                stack.append(bracket_idx[c])
                
            # closing bracket
            else:
                try:
                    pop = stack.pop()
                    if pop + bracket_idx[c] != 0:
                        return False
                # if you try to close bracket without opening bracket
                except: 
                    return False
        
        return True if len(stack) == 0 else False
    
    
    answer = 0
    # check whether correct bracket of spinning string
    for _ in range(len(s)):
        s = s[1:]+s[0]
        result = isCorrectBracket(s)
        if result:
            answer = answer + 1

    return answer
