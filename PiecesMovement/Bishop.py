def BishopMovement(BoardPieces,Row,Col):
    directions = [
    (-1, -1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7)(-8,-8),
    (-1, 1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
    (1, -1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
    (1, 1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)
    ]

    BishopLegalMoves = []
    Bishop = BoardPieces[Row][Col]
    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Col + dc

        if not (0 <= NewRow < 8 and 0 <= NewCol < 8):
            continue
        print(NewRow, NewCol)

        target = BoardPieces[NewRow][NewCol]

        #if square has no piece on it
        if target == 0:
            BishopLegalMoves.append([NewRow,NewCol])

        elif Bishop > 0 and target < 0:
            BishopLegalMoves.append([NewRow,NewCol])

        elif Bishop < 0 and target > 0:
            BishopLegalMoves.append([NewRow,NewCol])

    return BishopLegalMoves