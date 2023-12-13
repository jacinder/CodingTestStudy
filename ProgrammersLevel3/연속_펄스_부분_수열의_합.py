def solution(sequence):
    answer = 0
    n = len(sequence)
    
    seq1 = [sequence[i] * (-1) ** i for i in range(n)]
    seq2 = [sequence[i] * (-1) ** (i+1) for i in range(n)]

    
    for i in range(1,n):
        seq1[i] = max(seq1[i-1]+seq1[i], seq1[i])
        seq2[i] = max(seq2[i-1]+seq2[i], seq2[i])
    
    
    answer = max(max(seq1), max(seq2))
    return answer

