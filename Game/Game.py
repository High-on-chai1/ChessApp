def GetNumberBoard():
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



def Notation(PieceNumber,Board):
    if PieceNumber < 0:
        PieceNumber = PieceNumber * (-1)
    
    PieceType =['','B','N','R','Q','K']

    return PieceType[PieceNumber - 1]
    #will implement disambiguation and other such features later, this is only a proof of concept



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



def KingMovement(BoardPieces, SRow, SCol, ERow=None, ECol=None):
    directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]
    KingLegalMoves = []
    King = BoardPieces[SRow][SCol]
    
    for dr, dc in directions:
        NewRow = SRow + dr
        NewCol = SCol + dc
    
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

    if (ERow == 7 and (ECol == 6 or  ECol == 2)) or (ERow == 0 and (ECol == 6 or ECol == 2)):
        CastlingRules(SRow, SCol, ERow, ECol)

    IllegalMoves = IsSquareTargeted(ERow,ECol,King)

    KingLegalMoves = [move for move in LegalMoves if move not in IllegalMoves]  #[ move      for move in LegalMoves     if move not in IllegalMoves  ]
#                                                                                   ↑              ↑                         ↑
#                                                                                 keep this    go through these          only keep if true      
    return KingLegalMoves



def KnightMovement(BoardPieces, Row, Col):
    directions =[( 2, 1),(-2,-1),
                 ( 1, 2),(-1,-2),
                 ( 2,-1),(-2, 1),
                 (-1, 2),( 1,-2)
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
            KnightLegalMoves.append([NewRow, NewCol])

        elif Knight > 0 and target < 0:
            KnightLegalMoves.append([NewRow, NewCol])

        elif Knight < 0 and target > 0:
            KnightLegalMoves.append([NewRow, NewCol])

            
    return KnightLegalMoves



def PawnMovement(BoardPieces, Row, Col):
    directions = [
        (1,0), (1,1), (1,-1)
    ]

    PawnLegalMoves = []
    Pawn = BoardPieces[Row][Col]

    if Row == 6 and BoardPieces[5][Col] == 0 and BoardPieces[4][Col] == 0 and Pawn == 1: 
         PawnLegalMoves.append([Row + 2,Col])

    elif Row == 1 and BoardPieces[2][Col] == 0 and BoardPieces[3][Col] == 0 and Pawn == -1:
         PawnLegalMoves.append([Row - 2, Col])


    for dr, dc in directions:
        if Pawn == -1:
            NewRow = Row - dr
            NewCol = Col + dc
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

def CastlingRules(SRow,SCol,ERow,ECol): #not fully completed, need to make sure selected piece is king and no pieces in between WIP
    
    if KingMoved == False and (ERow == 7 and ECol == 6) and (SRow == 7 and SCol == 4) and RooksMoved[3] == False and NumberBoard[SRow][SCol + 1] == NumberBoard[SRow][SCol + 2] == 0: #White KingSide
        LegalMoves[5].append([7,6])
        KingMoved[0] = True
        RooksMoved[3] = True

    elif KingMoved == False and (ERow == 7 and ECol == 2) and (SRow == 7 and SCol == 4) and RooksMoved[2] == False and NumberBoard[SRow][SCol - 1] == NumberBoard[SRow][SCol - 2] == NumberBoard[SRow][SCol - 3] == 0: #White QueenSide
        LegalMoves[5].append([7,2])
        KingMoved[0] = True
        RooksMoved[2] = True

    elif KingMoved == False and (ERow == 0 and ECol == 6) and (SRow == 0 and SCol == 4) and RooksMoved[1] == False and NumberBoard[SRow][SCol + 1] == NumberBoard[SRow][SCol + 2] == 0: #Black KingSide
        LegalMoves[5].append([0,6])
        KingMoved[1] = True
        RooksMoved[1] = True

    elif KingMoved == False and (ERow == 0 and ECol == 2) and (SRow == 0 and SCol == 4) and RooksMoved[0] == False and NumberBoard[SRow][SCol - 1] == NumberBoard[SRow][SCol - 2] == NumberBoard[SRow][SCol - 3] == 0: #Black Queen Side
        LegalMoves[5].append([0,2])
        KingMoved[1] = True
        RooksMoved[0] = True
    
def IsSquareTargeted(ERow, ECol, KingColor): #WIP

    PseudoLegalMoves = []

    RBishopV = BishopMovement(NumberBoard,ERow,ECol) #RBishopV stands for Reverse Bishop Vision same convention will be used for all pieces
    RKnightV = KnightMovement(NumberBoard,ERow,ECol)
    RRookV = RookMovement(NumberBoard,ERow,ECol)
    RQueenV = QueenMovement(NumberBoard,ERow,ECol)
    RKingV = KingMovement(NumberBoard,ERow,ECol)

    if KingColor < 0:
        if (ReverseIteration(RBishopV, 2)):
            PseudoLegalMoves.append([ERow,ECol])

        if (ReverseIteration(RKnightV, 3)):
            PseudoLegalMoves.append([ERow,ECol])
            
        if (ReverseIteration(RRookV, 4)):
            PseudoLegalMoves.append([ERow,ECol])

        if (ReverseIteration(RQueenV, 5)):
            PseudoLegalMoves.append([ERow,ECol])

        if(ReverseIteration(RKingV, 6)):
            PseudoLegalMoves.append([ERow,ECol])

        if NumberBoard[ERow + 1][ECol - 1] == 1 or NumberBoard[ERow + 1][ECol + 1] == 1:
            PseudoLegalMoves.append([ERow,ECol])


    elif KingColor > 0:
        if (ReverseIteration(RBishopV, -2)):
            PseudoLegalMoves.append([ERow,ECol])

        if (ReverseIteration(RKnightV, -3)):
            PseudoLegalMoves.append([ERow,ECol])

        if (ReverseIteration(RRookV, -4)):
            PseudoLegalMoves.append([ERow,ECol])

        if (ReverseIteration(RQueenV, -5)):
            PseudoLegalMoves.append([ERow,ECol])

        if (ReverseIteration(RKingV, -6)):
            PseudoLegalMoves.append([ERow,ECol])

        if NumberBoard[ERow - 1][ECol - 1] == -1 or NumberBoard[ERow - 1][ECol + 1] == -1:
            PseudoLegalMoves.append([ERow,ECol])

    return PseudoLegalMoves

    

def ReverseIteration(MoveList, PieceType): #WIP

    for Row, Col in MoveList:
        if NumberBoard[Row][Col] == PieceType:
            return True
    return False



def CastlingMove(Row,Col):
    print('idk man') #WIP


print("Enter Move in the format: Starting Square, Ending Square (e.g. A2,A4)")
Count = 0
WhiteTurn = False
BlackTurn = False
NumberBoard = GetNumberBoard()

KingMoved = [False,False] # 0: White King, 1: Black King
RooksMoved = [False,False, 
              False,False]

while True:
    Index = []
    LegalMoves = []

    Movement = []
    if Count % 2 == 0:
        print("White Move: ")
        Move = str(input("Enter the move: "))
        WhiteTurn = True
        BlackTurn = False
    else:
        print("Black Move: ")
        Move = str(input("Enter the move: "))
        BlackTurn = True
        WhiteTurn = False

    Movement = Move.split(",")
    StartSq = Movement[0]
    EndSq = Movement[1]

    StartIndex = FindIndex(StartSq)
    Piece = NumberBoard[StartIndex[0]][StartIndex[1]]
    EndIndex = FindIndex(EndSq)

    LegalMoves.append(PawnMovement(NumberBoard,StartIndex[0],StartIndex[1]))
    LegalMoves.append(BishopMovement(NumberBoard,StartIndex[0],StartIndex[1]))
    LegalMoves.append(KnightMovement(NumberBoard,StartIndex[0],StartIndex[1]))
    LegalMoves.append(RookMovement(NumberBoard,StartIndex[0],StartIndex[1]))
    LegalMoves.append(QueenMovement(NumberBoard,StartIndex[0],StartIndex[1]))
    LegalMoves.append(KingMovement(NumberBoard,StartIndex[0],StartIndex[1],EndIndex[0],EndIndex[1]))

    if EndIndex in LegalMoves[Piece - 1] and WhiteTurn == True and Piece > 0:
            NumberBoard[StartIndex[0]][StartIndex[1]] = 0
            NumberBoard[EndIndex[0]][EndIndex[1]] = Piece

            print(f"{Notation(Piece)}{EndSq}") #algebraic notation for movement of pieces
            
            Count += 1
            if Piece == 6:
                KingMoved[0] = True
        
    if EndIndex in LegalMoves[(Piece * -1) - 1] and BlackTurn == True and Piece < 0:
            NumberBoard[StartIndex[0]][StartIndex[1]] = 0
            NumberBoard[EndIndex[0]][EndIndex[1]] = Piece

            print(f"{Notation(Piece)}{EndSq}") #algebraic notation for movement of pieces

            Count += 1
            if Piece == -6:
                KingMoved[1] = True

#To do, castling, en passant, checks, pins, promotion. not in order.