# Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.
# The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically 
# and one square horizontally away from it. The complete move therefore looks like the letter L. 
# Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

def chessKnight(cell):
    knX,knY = ord(cell[0]),int(cell[1])
    #------slope of the moves of a knight
    m_NE_SW_low = 0.5 
    m_NE_SW_high = 2
    
    m_NW_SE_low = -0.5
    m_NW_SE_high = -2
    #-------------b------------------------
    #b for quad 1 and 3
    b_NE_low = knY - (m_NE_SW_low * knX) 
    b_NE_high = knY - (m_NE_SW_high * knX) 
    
    #b for quad 2 and 4
    b_NW_low = knY - (m_NW_SE_low * knX)
    b_NW_high = knY - (m_NW_SE_high * knX)
    valid_moves = []
    for posX in range(97,105):
        for posY in range(1,9):
        #Checker
            if posY == (m_NE_SW_high * posX) + b_NE_high or \
               posY == (m_NE_SW_low * posX) + b_NE_low or \
               posY == (m_NW_SE_high * posX) + b_NW_high or \
               posY == (m_NW_SE_low * posX) + b_NW_low:
                if (abs(knY - posY) == 1 or abs(knY - posY) == 2) \
                    and (abs(knX - posX) == 1 or abs(knX - posX) == 2):
                    valid_moves.append((chr(posX)+str(posY)))
    return len(valid_moves)
