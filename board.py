import numpy as np #the structure used for storing the board is an np array
import pygame
ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER_PIECE=1
AI_PIECE=2

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT)) #initializaing an empty array
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT): #starting from 0 to the row count we check for and empty row of the chosen column
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))


def winning_score(board, piece):
    score=0
    #Horizontal win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                score+=1

    # Vertical win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                score+=1

    # right digonal win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                score+=1

    # left digonal win
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                score+=1
    return score


#RED is 1
#yellow is 2
# AI FUNCTIONS

def get_Children(board): #get the children of the current board (vary from 0 to 7 ) and check if the child is valid
    children=[]
    for col in range(COLUMN_COUNT):
        if(is_valid_location(board,col)):
            children.append(col)

    return children

def is_terminal_node(board):
    return np.count_nonzero(board) == 42 #if the board has no empty places then the game is over (terminal node)

def scores(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    if window.count(piece) == 4:
        score += 110 #win
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 60 #empty place and 3 in a row
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 10 #2 in a row and 2 empty places

    if window.count(opp_piece) == 4:
        score -= 100 # opponent win
    elif window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 50  # opponent connect 3
    elif window.count(opp_piece) == 2 and window.count(0) == 2:
        score -= 5   # opponent connect 2

    return score

def hurestic(board,piece):
    hueristic_array = np.array(
        [[0.25, 0.5, 1, 2, 1, 0.5, 0.25], [0.5, 1, 2, 3, 2, 1, 0.5], [1, 1.5, 2.5, 4, 2.5, 1.5, 1],
         [1, 1.5, 2.5, 4, 2.5, 1.5, 1], [0.5, 1, 2, 3, 2, 1, 0.5], [0.25, 0.5, 1, 2, 1, 0.5, 0.25]])

    copy_board = board.copy()

    score=0
    # To favor playing the middle places we multiply the current board with the heuristic array to get a score
    #note that playing in the middle should be favored because it provides more opportunity for a win
    if piece == AI_PIECE :
         copy_board[copy_board == PLAYER_PIECE] = 0
         copy_board[copy_board == AI_PIECE]=1
         score+=np.sum(np.multiply(copy_board,hueristic_array))
    else:
         copy_board[copy_board == AI_PIECE] = 0
         score+=np.sum(np.multiply(copy_board,hueristic_array))

    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c + 4]   #assign the row to a window for score calculation later
            score += scores(window, piece)#send the list (window) for score evaluation

    ## Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r + 4]
            score += scores(window, piece)

    ## Score posiive sloped diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += scores(window, piece)

    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + 3 - i][c + i] for i in range(4)]
            score += scores(window, piece)



    return score

#board GUI part
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)
screen = pygame.display.set_mode(size)

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, (0, 0, 0), (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()
