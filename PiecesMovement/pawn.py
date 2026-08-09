def PawnMovement(BoardPieces,Row,Col):
    directions = [
        (1,0), (1,1), (1,-1), (2,0)
    ]

    PawnLegalMoves = []
    Pawn = BoardPieces[Row][Col]

    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Row + dc

        if not (0 <= NewRow < 8 and 0 <= NewCol < 8):
            continue
        print(NewRow, NewCol)

        target = BoardPieces[NewRow][NewCol]

        if target == 0:
            PawnLegalMoves.append([NewRow, NewCol])

        elif ((dr, dc) == (1,1) or (dr,dc) == (1,-1)) and (Pawn > 0 and target < 0)
                PawnLegalMoves.append([NewRow, NewCol])

        elif ((dr, dc) == (1,1) or (dr,dc) == (1,-1)) and (Pawn < 0 and target > 0):
                PawnLegalMoves.append([NewRow, NewCol])

    return PawnLegalMoves