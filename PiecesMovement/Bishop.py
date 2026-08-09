def BishopMovement(BoardPieces, Row, Col):
    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    BishopLegalMoves = []
    Bishop = BoardPieces[Row][Col]

    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Col + dc

        while 0 <= NewRow < 8 and 0 <= NewCol < 8:
            target = BoardPieces[NewRow][NewCol]

            if target == 0:
                BishopLegalMoves.append([NewRow, NewCol])

            elif Bishop > 0 and target < 0:
                BishopLegalMoves.append([NewRow, NewCol])
                break

            elif Bishop < 0 and target > 0:
                BishopLegalMoves.append([NewRow, NewCol])
                break

            else:
                break

            NewRow += dr
            NewCol += dc

    return BishopLegalMoves