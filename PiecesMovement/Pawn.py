def PawnMovement(BoardPieces,Row,Col):
    directions = [
        (1,0), (1,1), (1,-1)
    ]

    PawnLegalMoves = []
    Pawn = BoardPieces[Row][Col]

    if Row == 6 and BoardPieces[5][Col] == 0 and BoardPieces[4][Col] == 0: #added double pawn movement seperately
         PawnLegalMoves.append([Row + 2,Col])

    elif Row == 1 and BoardPieces[2][Col] == 0 and BoardPieces[3][Col] == 0:
         PawnLegalMoves.append([Row - 2, Col])


    for dr, dc in directions:
        if Pawn == -1:
            NewRow = Row - dr
            NewCol = Col - dc
        else:
            NewRow = Row + dr
            NewCol = Col + dc

        if not (0 <= NewRow < 8 and 0 <= NewCol < 8):
            continue
        print(NewRow, NewCol)

        target = BoardPieces[NewRow][NewCol]

        if (dr, dc) == (1,0) and target == 0:
            PawnLegalMoves.append([NewRow, NewCol])

        elif ((dr, dc) == (1,1) or (dr,dc) == (1,-1)) and (Pawn > 0 and target < 0):
                PawnLegalMoves.append([NewRow, NewCol])

        elif ((dr, dc) == (1,1) or (dr,dc) == (1,-1)) and (Pawn < 0 and target > 0):
                PawnLegalMoves.append([NewRow, NewCol])

    return PawnLegalMoves

#I plan to make most of these checks into modular functions so I can effortlessly use them in 
#Pins to the king and I guess thats about it