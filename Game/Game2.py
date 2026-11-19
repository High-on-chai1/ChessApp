"""
Extracted reusable parts of the original chess project.

Preserved:
- Signed-integer board representation
- Original 8x8 coordinate convention (row 0 = rank 8, row 7 = rank 1)
- Basic movement generation for all six piece types
- Basic notation and square conversion

Intentionally not included:
- Castling (original implementation was incomplete and changed rights while
  merely checking a move)
- The original IsSquareTargeted implementation (marked WIP and coupled to
  incomplete king/castling logic)
- The terminal game loop

Important:
These are pseudo-legal movement generators, not a complete legal chess engine.
They do not yet enforce king safety, pins, en passant, promotion, or game endings.
"""

def get_number_board():
    """Return the starting board. Positive = White, negative = Black."""
    return [
        [-4, -3, -2, -5, -6, -2, -3, -4],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 1,  1,  1,  1,  1,  1,  1,  1],
        [ 4,  3,  2,  5,  6,  2,  3,  4],
    ]


def get_letter_board():
    """Return square names in the same orientation as the numeric board."""
    return [
        ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"],
        ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
        ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
        ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
        ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
        ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
        ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
        ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"],
    ]


def notation(piece_number, board=None):
    """Return the piece letter used by the original proof-of-concept notation."""
    piece_type = ["", "B", "N", "R", "Q", "K"]
    return piece_type[abs(piece_number) - 1]


def find_index(destination_square):
    """Convert a square such as 'E4' to [row, column], or return None."""
    if not isinstance(destination_square, str):
        return None

    square = destination_square.strip().upper()
    if len(square) != 2:
        return None

    file_letter, rank = square[0], square[1]
    if file_letter not in "ABCDEFGH" or rank not in "12345678":
        return None

    return [8 - int(rank), ord(file_letter) - ord("A")]


def bishop_movement(board, coordinates):
    row, col = coordinates[:2]
    piece = board[row][col]
    moves = []

    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        new_row, new_col = row + dr, col + dc

        while 0 <= new_row < 8 and 0 <= new_col < 8:
            target = board[new_row][new_col]

            if target == 0:
                moves.append([new_row, new_col])
            elif piece > 0 and target < 0:
                moves.append([new_row, new_col])
                break
            elif piece < 0 and target > 0:
                moves.append([new_row, new_col])
                break
            else:
                break

            new_row += dr
            new_col += dc

    return moves


def knight_movement(board, coordinates):
    row, col = coordinates[:2]
    piece = board[row][col]
    moves = []

    for dr, dc in [
        (2, 1), (-2, -1), (1, 2), (-1, -2),
        (2, -1), (-2, 1), (-1, 2), (1, -2),
    ]:
        new_row, new_col = row + dr, col + dc

        if not (0 <= new_row < 8 and 0 <= new_col < 8):
            continue

        target = board[new_row][new_col]
        if target == 0 or (piece > 0 and target < 0) or (piece < 0 and target > 0):
            moves.append([new_row, new_col])

    return moves


def pawn_movement(board, coordinates):
    row, col = coordinates[:2]
    pawn = board[row][col]
    moves = []

    # Forward movement and initial two-square move.
    direction = -1 if pawn > 0 else 1
    start_row = 6 if pawn > 0 else 1
    one_step = row + direction

    if 0 <= one_step < 8 and board[one_step][col] == 0:
        moves.append([one_step, col])

        two_step = row + 2 * direction
        if row == start_row and board[two_step][col] == 0:
            moves.append([two_step, col])

    # Diagonal captures.
    for dc in (-1, 1):
        new_row, new_col = row + direction, col + dc
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            target = board[new_row][new_col]
            if (pawn > 0 and target < 0) or (pawn < 0 and target > 0):
                moves.append([new_row, new_col])

    return moves


def queen_movement(board, coordinates):
    row, col = coordinates[:2]
    piece = board[row][col]
    moves = []

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        while 0 <= new_row < 8 and 0 <= new_col < 8:
            target = board[new_row][new_col]

            if target == 0:
                moves.append([new_row, new_col])
            elif (piece > 0 and target < 0) or (piece < 0 and target > 0):
                moves.append([new_row, new_col])
                break
            else:
                break

            new_row += dr
            new_col += dc

    return moves


def rook_movement(board, coordinates):
    row, col = coordinates[:2]
    piece = board[row][col]
    moves = []

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + dr, col + dc

        while 0 <= new_row < 8 and 0 <= new_col < 8:
            target = board[new_row][new_col]

            if target == 0:
                moves.append([new_row, new_col])
            elif (piece > 0 and target < 0) or (piece < 0 and target > 0):
                moves.append([new_row, new_col])
                break
            else:
                break

            new_row += dr
            new_col += dc

    return moves


def king_movement(board, coordinates):
    """
    Generate adjacent king moves only.

    Check filtering and castling are deliberately excluded until the
    attack-detection and special-move systems are implemented.
    """
    row, col = coordinates[:2]
    king = board[row][col]
    moves = []

    for dr, dc in [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]:
        new_row, new_col = row + dr, col + dc

        if not (0 <= new_row < 8 and 0 <= new_col < 8):
            continue

        target = board[new_row][new_col]
        if target == 0 or (king > 0 and target < 0) or (king < 0 and target > 0):
            moves.append([new_row, new_col])

    return moves


MOVEMENT_FUNCTIONS =[
    pawn_movement,
    bishop_movement,
    knight_movement,
    rook_movement,
    queen_movement,
    king_movement,
]


def get_piece_moves(board, position):
    """Get pseudo-legal moves for the piece at [row, column]."""
    row, col = position
    piece = board[row][col]

    if piece == 0:
        return []

    return MOVEMENT_FUNCTIONS[abs(piece) - 1](board, position)


def BQ_target_check(board, R, C, color):
    while R < 8 and C < 8 and R >= 0 and C >= 0:
        if board[R][C] == 0:
            continue
        elif abs(board[R][C]) == 2 or abs(board[R][C]) == 5:
            if color > 0 and board[R][C] < 0:
                    return True
            elif color < 0 and board[R][C] > 0:
                    return True
            else:
                  break
        elif color > 0 and board[R][C] > 0:
            break
        elif color < 0 and board[R][C] < 0:
            break
        else:
            break


def RQ_target_check(board, R, C, color):
    while R < 8 and C < 8 and R >= 0 and C >= 0: #checks if a rook or queen exists at square R,C
        if board[R][C] == 0:
            continue
        elif abs(board[R][C]) == 4 or abs(board[R][C]) == 5:
            if color > 0 and board[R][C] < 0:
                    return True
            elif color < 0 and board[R][C] > 0:
                    return True
            else:
                  break
        elif color > 0 and board[R][C] > 0:
            break
        elif color < 0 and board[R][C] < 0:
            break
        else:
            break


def is_square_targeted(board, coordinates, color):
    Attacked = False
    '''Bishop/Queen Diagonal'''
    R, C = coordinates[0], coordinates[1] #checking all four diagonals for a bishop or queen attack
    for i in range(8):
        while R < 8 and C < 8 and R >= 0 and C >= 0:
            R =+1
            C =+1
            Attacked = BQ_target_check(board, R, C, color)          


    R, C = coordinates[0], coordinates[1]    
    for i in range(8):
        while R < 8 and C < 8 and R >= 0 and C >= 0:
            R =+1
            C =-1
            Attacked = BQ_target_check(board, R, C, color)


    R, C = coordinates[0], coordinates[1]    
    for i in range(8):
        while R < 8 and C < 8 and R >= 0 and C >= 0:
            R =-1
            C =-1
            Attacked = BQ_target_check(board, R, C, color)


    R, C = coordinates[0], coordinates[1]    
    for i in range(8):
        while R < 8 and C < 8 and R >= 0 and C >= 0:
            R =-1
            C =+1
            Attacked = BQ_target_check(board, R, C, color)
            

    '''Rook/Queen Straight'''
    R, C = coordinates[0], coordinates[1] #checking all 4 directions for a rook or queen attack
    for i in range(8):
        while R < 8 and C < 8 and R >= 0 and C >= 0:
            R =+1
            Attacked = RQ_target_check(board, R, C, color)
        
    R, C = coordinates[0], coordinates[1]
    for i in range(8):
        while R < 8 and C < 8 and R >= 0 and C >= 0:
            R =-1
            Attacked = RQ_target_check(board, R, C, color)

    R, C = coordinates[0], coordinates[1]
    for i in range(8):
        while R < 8 and C < 8 and R >= 0 and C >= 0:
            C =+1
            Attacked = RQ_target_check(board, R, C, color)

    R, C = coordinates[0], coordinates[1]
    for i in range(8):
        while R < 8 and C < 8 and R >= 0 and C >= 0:
            C =-1
            Attacked = RQ_target_check(board, R, C, color)

    
    '''Knight Check'''
    R, C = coordinates[0], coordinates[1]
    for dr, dc in [
        (2, 1), (-2, -1), (1, 2), (-1, -2), #checking if a knight exists in any of the 8 possible knight move positions from the square
        (2, -1), (-2, 1), (-1, 2), (1, -2),
    ]:
        new_row, new_col = R + dr, C + dc

        if not (0 <= new_row < 8 and 0 <= new_col < 8):
            continue

        target = board[new_row][new_col]
        if (color > 0 and target == -3) or (color < 0 and target == 3):
            Attacked = True


    '''Pawn Check'''
    R, C = coordinates[0], coordinates[1]
    if color > 0:
        if board[R - 1][C - 1] == -1 or board[R + 1][C - 1] == -1: #if the color is white, check if pawn exists diagonally one back from it on both directions
            Attacked = True
    elif color < 0:
        if board[R - 1][C + 1] == 1 or board[R + 1][C + 1] == 1: #same for black
            Attacked = True


    '''King Check'''
    R, C = coordinates[0], coordinates[1]
    for dr, dc in [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]:
        new_row, new_col = R + dr, C + dc

        if not (0 <= new_row < 8 and 0 <= new_col < 8):
            continue

        target = board[new_row][new_col]
        if (color > 0 and target == -6) or (color < 0 and target == 6):
            Attacked = True

            
    return Attacked

