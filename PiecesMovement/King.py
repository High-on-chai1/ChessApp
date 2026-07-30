
def KingMovement(BoardPieces,Row,Col):
    directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]
    KingLegalMoves = []
    King = BoardPieces[Row][Col]

    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Col + dc
    
        if not (0 <= NewRow < 8 and 0 <= NewCol < 8):
            continue
        print(NewRow, NewCol)

        target = BoardPieces[NewRow][NewCol]

        #If the square has no piece on it
        if target == 0:
            KingLegalMoves.append([NewRow, NewCol])
        
        #Whit King Black pieces
        elif King > 0 and target < 0:
            KingLegalMoves.append([NewRow, NewCol])

        #opposite of above
        elif King < 0 and target > 0:
            KingLegalMoves.append([NewRow, NewCol])
#fyi we dont check for our own pieces or same pieces because taking that is an illegal move

    return KingLegalMoves

#this is the basic movement for the king still needs much more
#such as letter coordinate to actual coordinate translation and pins and
#if the enemy piece is protected 


#also what to do in checks but we need to make all other pieces before that and pinds
#ps I had no wifi for a couple hours so I did all of this (was bored)