def RookMovement(BoardPieces, Row, Col):
    directions = [
        (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
        (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0),
        (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
        (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8)
    ]

    RookLegalMoves = []
    Rook = BoardPieces[Row][Col]
    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Col + dc

        if not(0 <= NewRow < 8 and 0 <= NewCol < 8):
            continue 
        print(NewRow,NewCol)

        target = BoardPieces[NewRow][NewCol]

        if target == 0:
            RookLegalMoves.append([NewRow][NewCol])

        elif Rook > 0 and target < 0:
            RookLegalMoves.append([NewRow][NewCol])

        elif Rook < 0 and target > 0:
            RookLegalMoves.append([NewRow][NewCol])

    return RookLegalMoves