def sudoku(grid):
    #boxes
    myLst = []
    for lst in range(3,10,3):
        end = 3
        st = 0
        for elm in range(3):
            temp = grid[lst-3][st:end]+grid[lst-2][st:end]+grid[lst-1][st:end]
            set_temp = set(temp)
            if len(list(set_temp)) != len(temp):
                myLst.append(False)
            end += 3
            st += 3
    #rows
    for lst in range(len(grid)):
        if len(set(grid[lst])) != len(grid[lst]):
            myLst.append(False)

    #col
    for col in range(len(grid)):
        x = [grid[0][col],grid[1][col],grid[2][col],grid[3][col],\
            grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]]
        if len(set(x)) != len(x):
            myLst.append(False)

    if len(myLst) == 0:
        return True
    return False