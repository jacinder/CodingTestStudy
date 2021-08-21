def solution(arr1, arr2):


    row1 = len(arr1)
    col1 = len(arr1[0])
    row2 = len(arr2)
    col2 = len(arr2[0])
    print(row1)
    print(col1)

    answer = []

    for i in range(row1):
        mul_matrix = []
        for k in range(col2):
            mul_element = 0
            for j in range(col1):
                mul_element += arr1[i][j]*arr2[j][k]
            mul_matrix.append(mul_element)
        answer.append(mul_matrix)


    return answer
