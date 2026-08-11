def NumberBoard():
    BoardNumber = [[-4,-3,-2,-5,-6,-2,-3,-4],
                   [-1,-1,-1,-1,-1,-1,-1,-1],
                   [ 0, 0, 0, 0, 0, 0, 0, 0],
                   [ 0, 0, 0, 0, 0, 0, 0, 0],
                   [ 0, 0, 0, 0, 0, 0, 0, 0],
                   [ 0, 0, 0, 0, 0, 0, 0, 0],
                   [ 1, 1, 1, 1, 1, 1, 1, 1],
                   [ 4, 3, 2, 5, 6, 2, 3, 4]]
    for row in BoardNumber:
        print(row)


def GetLetterBoard():
    LetterBoard = [
        ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"],
        ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
        ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
        ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
        ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
        ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
        ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
        ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]
    ]

    return LetterBoard




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

    return KingLegalMoves



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




print("Enter Move in the format: Starting Square, Ending Square (e.g. A2,A4)")
count = 0
while True:
    Movement = []
    if count % 2 == 0:
        print("White Move: ")
        Move = str(input("Enter the move: "))
    else:
        print("Black Move: ")
        Move = str(input("Enter the move: "))
    count += 1

    Movement = Move.split(",")
    EndSq = Movement[1]
    if EndSq in LegalMoves: