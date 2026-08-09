def RookMovement(BoardPieces, Row, Col):
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    RookLegalMoves = []
    Rook = BoardPieces[Row][Col]

    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Col + dc

        while 0 <= NewRow < 8 and 0 <= NewCol < 8:
            target = BoardPieces[NewRow][NewCol]

            if target == 0:
                RookLegalMoves.append([NewRow, NewCol])

            elif Rook > 0 and target < 0:
                RookLegalMoves.append([NewRow, NewCol])
                break

            elif Rook < 0 and target > 0:
                RookLegalMoves.append([NewRow, NewCol])
                break

            else:
                break

            NewRow += dr
            NewCol += dc

    return RookLegalMoves