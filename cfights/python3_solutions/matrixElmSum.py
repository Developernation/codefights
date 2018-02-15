def matrixElementsSum(matrix):
    out_list = []

    for item in range(len(matrix)):
        for num in range(len(matrix[item])):
            try:
                if matrix[item].index(matrix[item][num],num) == matrix[item].index(0,num):
                    if item+1 < len(matrix):
                        matrix[item+1][num] = 0
            except Exception:
                pass
    for lst in matrix:
        out_list += lst
    
    return(sum(out_list))
