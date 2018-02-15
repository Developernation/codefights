#Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

def differentSquares(matrix):
    if len(matrix) <= 1:
        return 0 
    d = set()
    for elm in range(1,len(matrix)):
        for item in range(1,len(matrix[elm])):
            temp_lst = ''.join([str(matrix[elm-1][item-1]),str(matrix[elm-1][item]),
                        str(matrix[elm][item-1]),str(matrix[elm][item])])
            print(d.add(temp_lst))
    return(len(d))