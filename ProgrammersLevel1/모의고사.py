def solution(answers):
    anslen = len(answers)
    
    pattern = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    patlen = [5,8,10]
    supoza = [[],[],[]]
    score = [0,0,0]

    # make supoza answer sheet
    for i in range(3):
        for _ in range(anslen // patlen[i]):
            supoza[i] += pattern[i]
        supoza[i] += pattern[i][:anslen % patlen[i]]

    # make the matching rank
    for i in range(anslen):
        for j in range(3):
            if answers[i] == supoza[j][i]:
                score[j] += 1

    answer = [i+1 for i, v in enumerate(score) if v == max(score)]
    return answer