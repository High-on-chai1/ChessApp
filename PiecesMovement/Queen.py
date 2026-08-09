def QueenMovement(BoardPieces, Row, Col):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    QueenLegalMoves = []
    Queen = BoardPieces[Row][Col]

    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Col + dc

        while 0 <= NewRow < 8 and 0 <= NewCol <8:
            target = BoardPieces[NewRow][NewCol]

            if target == 0:
                QueenLegalMoves.append([NewRow,NewCol])

            
            elif Queen > 0 and target < 0:
                QueenLegalMoves.append([NewRow, NewCol])
                break

            elif Queen < 0 and target > 0:
                QueenLegalMoves.append([NewRow, NewCol])
                break
            
            else:
                break

            NewRow += dr
            NewCol += dc

    return QueenLegalMoves
