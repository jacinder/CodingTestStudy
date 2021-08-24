def solution(s):
    n = s.split(' ')
    n = list(map(int, n))
    
    answer = f'{min(n)} {max(n)}'
    return answer