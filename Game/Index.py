from Boards.BoardLetters import *

def FindIndex(StartSquare):
    LetterBoard = GetLetterBoard()
    RowCount = 0
    ColCount = 0
    for _ in range(64):
        if LetterBoard[RowCount][ColCount] == StartSquare:
            return(f"{RowCount}, {ColCount}")
            
        RowCount += 1
        if RowCount == 8:
            ColCount += 1
            RowCount == 0
