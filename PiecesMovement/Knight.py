def KnightMovement(BoardPieces, Row, Col):
    directions =[( 2, 1),(-2,-1),
                 ( 1, 2),(-1,-2),
                 ( 2,-1),(-2, 1),
                 (-1, 2)( 1,-2)
    ]

    KnightLegalMoves = []
    Knight = BoardPieces[Row][Col]

    
    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Col + dc

        if not (0 <= NewRow < 8 and 0 <= NewCol < 8):
            continue
        print(NewRow, NewCol)

        target = BoardPieces[NewRow][NewCol]

        if target == 0:
            KnightLegalMoves.append(NewRow, NewCol)

        elif Knight > 0 and target < 0:
            KnightLegalMoves.append([NewRow, NewCol])

        elif Knight < 0 and target > 0:
            KnightLegalMoves.append([NewRow, NewCol])

            
    return KnightLegalMoves
