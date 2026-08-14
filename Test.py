def GetNumberBoard():
    BoardNumber = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    for row in BoardNumber:
        print(row)

    return BoardNumber



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



def Notation(PieceNumber, Board=None):
    if PieceNumber < 0:
        PieceNumber = PieceNumber * (-1)

    PieceType = ['', 'B', 'N', 'R', 'Q', 'K']

    return PieceType[PieceNumber - 1]
    # will implement disambiguation and other such features later, this is only a proof of concept



def FindIndex(DestinationSquare):
    LetterBoard = GetLetterBoard()
    RowCount = 0
    ColCount = 0
    for _ in range(64):
        if LetterBoard[RowCount][ColCount] == DestinationSquare:
            return [RowCount, ColCount]

        RowCount += 1
        if RowCount == 8:
            ColCount += 1
            RowCount = 0



def BishopMovement(BoardPieces, Row, Col, ReverseColour=None):
    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    BishopLegalMoves = []
    Bishop = BoardPieces[Row][Col]

    # When called from IsSquareTargeted the origin square is usually empty (0),
    # so neither the "Bishop > 0" nor "Bishop < 0" branch below would ever match.
    # ReverseColour lets the caller simulate a bishop of a given colour sitting there.
    if ReverseColour is not None:
        Bishop = 2 if ReverseColour > 0 else -2

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



def KingMovement(BoardPieces, Row, Col, ReverseColour=None):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    KingLegalMoves = []
    King = BoardPieces[Row][Col]

    if ReverseColour is not None:
        King = 6 if ReverseColour > 0 else -6

    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Col + dc

        if not (0 <= NewRow < 8 and 0 <= NewCol < 8):
            continue

        target = BoardPieces[NewRow][NewCol]

        # If the square has no piece on it
        if target == 0:
            KingLegalMoves.append([NewRow, NewCol])

        # White King, Black pieces
        elif King > 0 and target < 0:
            KingLegalMoves.append([NewRow, NewCol])

        # opposite of above
        elif King < 0 and target > 0:
            KingLegalMoves.append([NewRow, NewCol])

    # Only filter for check when this is a REAL king generating its own moves.
    # When ReverseColour is set we're inside IsSquareTargeted's reverse-vision
    # trick, and calling IsSquareTargeted again here would recurse forever.
    if ReverseColour is None:
        KingLegalMoves = [
            move for move in KingLegalMoves
            if not IsSquareTargeted(move[0], move[1], King)
        ]

    return KingLegalMoves



def KnightMovement(BoardPieces, Row, Col, ReverseColour=None):
    directions = [(2, 1), (-2, -1),
                  (1, 2), (-1, -2),
                  (2, -1), (-2, 1),
                  (-1, 2), (1, -2)
                  ]

    KnightLegalMoves = []
    Knight = BoardPieces[Row][Col]
    if ReverseColour is not None:
        Knight = 3 if ReverseColour > 0 else -3

    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Col + dc

        if not (0 <= NewRow < 8 and 0 <= NewCol < 8):
            continue

        target = BoardPieces[NewRow][NewCol]

        if target == 0:
            KnightLegalMoves.append([NewRow, NewCol])

        elif Knight > 0 and target < 0:
            KnightLegalMoves.append([NewRow, NewCol])

        elif Knight < 0 and target > 0:
            KnightLegalMoves.append([NewRow, NewCol])

    return KnightLegalMoves



def PawnMovement(BoardPieces, Row, Col):
    directions = [
        (1, 0), (1, 1), (1, -1)
    ]

    PawnLegalMoves = []
    Pawn = BoardPieces[Row][Col]

    # Double-step: white (Pawn == 1) starts on row 6 and advances toward row 0,
    # black (Pawn == -1) starts on row 1 and advances toward row 7.
    if Row == 6 and BoardPieces[5][Col] == 0 and BoardPieces[4][Col] == 0 and Pawn == 1:
        PawnLegalMoves.append([Row - 2, Col])

    elif Row == 1 and BoardPieces[2][Col] == 0 and BoardPieces[3][Col] == 0 and Pawn == -1:
        PawnLegalMoves.append([Row + 2, Col])

    for dr, dc in directions:
        if Pawn == 1:
            NewRow = Row - dr
            NewCol = Col + dc
        else:
            NewRow = Row + dr
            NewCol = Col + dc

        if not (0 <= NewRow < 8 and 0 <= NewCol < 8):
            continue

        target = BoardPieces[NewRow][NewCol]

        if (dr, dc) == (1, 0) and target == 0:
            PawnLegalMoves.append([NewRow, NewCol])

        elif ((dr, dc) == (1, 1) or (dr, dc) == (1, -1)) and (Pawn > 0 and target < 0):
            PawnLegalMoves.append([NewRow, NewCol])

        elif ((dr, dc) == (1, 1) or (dr, dc) == (1, -1)) and (Pawn < 0 and target > 0):
            PawnLegalMoves.append([NewRow, NewCol])

    return PawnLegalMoves



def QueenMovement(BoardPieces, Row, Col, ReverseColour=None):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    QueenLegalMoves = []
    Queen = BoardPieces[Row][Col]

    if ReverseColour is not None:
        Queen = 5 if ReverseColour > 0 else -5

    for dr, dc in directions:
        NewRow = Row + dr
        NewCol = Col + dc

        while 0 <= NewRow < 8 and 0 <= NewCol < 8:
            target = BoardPieces[NewRow][NewCol]

            if target == 0:
                QueenLegalMoves.append([NewRow, NewCol])

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



def RookMovement(BoardPieces, Row, Col, ReverseColour=None):
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    RookLegalMoves = []
    Rook = BoardPieces[Row][Col]

    if ReverseColour is not None:
        Rook = 4 if ReverseColour > 0 else -4

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


def IsSquareTargeted(ERow, ECol, KingColor):  # WIP
    PseudoLegalMoves = []

    # RBishopV stands for Reverse Bishop Vision, same convention used for all pieces.
    # Pass KingColor through as ReverseColour so each piece simulates itself as the
    # SAME colour as the king being checked, then looks for opposite-coloured
    # attackers landing on that square.
    RBishopV = BishopMovement(NumberBoard, ERow, ECol, KingColor)
    RKnightV = KnightMovement(NumberBoard, ERow, ECol, KingColor)
    RRookV = RookMovement(NumberBoard, ERow, ECol, KingColor)
    RQueenV = QueenMovement(NumberBoard, ERow, ECol, KingColor)
    RKingV = KingMovement(NumberBoard, ERow, ECol, ReverseColour=KingColor)

    if KingColor < 0:
        if ReverseIteration(RBishopV, 2):
            PseudoLegalMoves.append([ERow, ECol])

        if ReverseIteration(RKnightV, 3):
            PseudoLegalMoves.append([ERow, ECol])

        if ReverseIteration(RRookV, 4):
            PseudoLegalMoves.append([ERow, ECol])

        if ReverseIteration(RQueenV, 5):
            PseudoLegalMoves.append([ERow, ECol])

        if ReverseIteration(RKingV, 6):
            PseudoLegalMoves.append([ERow, ECol])

        if ERow + 1 < 8:
            left = ECol - 1 >= 0 and NumberBoard[ERow + 1][ECol - 1] == 1
            right = ECol + 1 < 8 and NumberBoard[ERow + 1][ECol + 1] == 1
            if left or right:
                PseudoLegalMoves.append([ERow, ECol])

    elif KingColor > 0:
        if ReverseIteration(RBishopV, -2):
            PseudoLegalMoves.append([ERow, ECol])

        if ReverseIteration(RKnightV, -3):
            PseudoLegalMoves.append([ERow, ECol])

        if ReverseIteration(RRookV, -4):
            PseudoLegalMoves.append([ERow, ECol])

        if ReverseIteration(RQueenV, -5):
            PseudoLegalMoves.append([ERow, ECol])

        if ReverseIteration(RKingV, -6):
            PseudoLegalMoves.append([ERow, ECol])

        if ERow - 1 >= 0:
            left = ECol - 1 >= 0 and NumberBoard[ERow - 1][ECol - 1] == -1
            right = ECol + 1 < 8 and NumberBoard[ERow - 1][ECol + 1] == -1
            if left or right:
                PseudoLegalMoves.append([ERow, ECol])

    return PseudoLegalMoves


def ReverseIteration(MoveList, PieceType):  # WIP
    for Row, Col in MoveList:
        if NumberBoard[Row][Col] == PieceType:
            return True
    return False


LegalMoves = []
NumberBoard = GetNumberBoard()
NumberBoard[1][1] = -4
print("----------------------------")
for row in NumberBoard:
    print(row)
print(IsSquareTargeted(2, 1, 1))