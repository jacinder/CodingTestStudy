from itertools import combinations
def solution(numbers, target):
    def dfs(numbers, target):
        if numbers == []:
            if target == 0:
                return 1
            else:
                return 0
        else:
            return dfs(numbers[1:], target-numbers[0])+dfs(numbers[1:], target+numbers[0])
                    
    answer = dfs(numbers, target)
    
    
    return answer
