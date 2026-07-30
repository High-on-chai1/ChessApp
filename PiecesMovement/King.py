
def KingMovement(BoardPieces,row,col):
    directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]
    LegalMoves = []
    King = BoardPieces[row][col]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
    
        if not (0 <= new_row < 8 and 0 <= new_col < 8):
            continue
        print(new_row, new_col)

        target = BoardPieces[new_row][new_col]

        #If the square has no piece on it
        if target == 0:
            LegalMoves.append(new_row, new_col)
        
        #Whit King Black pieces
        elif King > 0 and target < 0:
            LegalMoves.append(new_row, new_col)

        #opposite of above
        elif King < 0 and target > 0:
            LegalMoves.append(new_row, new_col)
#fyi we dont check for our own pieces or same pieces because taking that is an illegal move

    return LegalMoves

#this is the basic movement for the king still needs much more
#such as letter coordinate to actual coordinate translation and pins and
#if the enemy piece is protected 
#also what to do in checks but we need to make all other pieces before that and pinds
#ps I had no wifi for a couple hours so I did all of this (was bored)