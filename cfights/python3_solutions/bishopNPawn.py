# Given the positions of a white bishop and 
# a black pawn on the standard chess board, determine whether 
# the bishop can capture the pawn in one move.

# The bishop has no restrictions in distance for each move, 
# but is limited to diagonal movement. Check out the example 
# below to see how it can move:

def bishopAndPawn(bishop, pawn):
    bishX,bishY = ord(bishop[0]),int(bishop[1])
    pawnX,pawnY = ord(pawn[0]),int(pawn[1])

    b = bishY - bishX
    neg_b = bishY + bishX
    return (pawnY == pawnX + b) or (pawnY == (-1 * pawnX) + neg_b)