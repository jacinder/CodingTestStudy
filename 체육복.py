def solution(n, lost, reserve):
    
    
    delete = []
    for l in lost:
        if l in reserve:
            print(l)
            reserve.remove(l)
            delete.append(l)

    for l in delete:
        print(l)
        lost.remove(l)

    count = len(lost)
    # lost를 돌면서 -/+ 1인 값이 reserve에 있으면 그 값을 reserve에서 삭제하고 lost에서도 본인의 값을 삭제.
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            count -= 1

        elif l+1 in reserve:
            reserve.remove(l+1)
            count -= 1

    # n - len(lost)가 체육수업을 들을 수 있는 학생의 최댓값
    answer = n - count
    print(answer)
    return answer