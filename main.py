import numpy as np
import pygame
import board as b
import min_max as mi
import min_max as mai
import ctypes
import sys
import math
import time
from anytree import Node
deptho=2
deptho1 = 2
deptho2 = 2
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
pygame.init()
screen1 = pygame.display.set_mode((600, 600))
screen2 = pygame.display.set_mode((700, 600))
screen3 = pygame.display.set_mode((850, 600))

color_light = (170, 170, 170)
turn = 0
algorithmChoice=0
algorithmChoice1=0
algorithmChoice2=0
def startai():
    global turn
    board = b.create_board()
    b.print_board(board)
    game_over = False
    AI1 = 0
    AI2 = 1
    AI2_SCORE = 0
    AI1_SCORE = 0
    screen = pygame.display.set_mode(b.size)
    b.draw_board(board)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, b.width, b.SQUARESIZE))  # to clear circles
                posx = event.pos[0]

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, b.width, b.SQUARESIZE))
                # Ask for Player 1 Input

                if turn == AI1 and not game_over:
                    if b.is_terminal_node(board):
                        AI1_SCORE += b.winning_score(board, b.PLAYER_PIECE)
                        AI2_SCORE += b.winning_score(board, b.AI_PIECE)
                        game_over = True
                    global deptho1
                    root1 = Node(board)
                    start_time = time.time()
                    col, minimax_scorecore = mi.min_max_Function(board, deptho1, AI2, -math.inf, math.inf, root1,algorithmChoice1)
                    end_time = time.time()
                    print(
                        "time taken = " + str(end_time - start_time))  # calculate time taked and display it in console

                    if b.is_valid_location(board, col):
                        # pygame.time.wait(500)
                        row = b.get_next_open_row(board, col)
                        b.drop_piece(board, row, col, b.PLAYER_PIECE)

                        b.draw_board(board)
                        root1.name = str(minimax_scorecore) + "\n" + str(np.flip(board, 0))
                        # DotExporter(root).to_picture("udo.svg") #comment this line when we attempt depth more than 4
                        # os.system('udo.svg')
                        print("Nodes explored " + str(mi.count))
                        # print("leaf nodes  " + str(mi.leafs))
                        mi.count = 0
                        mi.counter=0
                        mi.leafs=0
                        turn += 1
                        turn = turn % 2
                        if b.is_terminal_node(board):
                            AI1_SCORE += b.winning_score(board, b.PLAYER_PIECE)
                            AI2_SCORE += b.winning_score(board, b.AI_PIECE)
                            turn=-1
                            game_over=True

                if turn == AI2 and not game_over:
                    if b.is_terminal_node(board):
                        AI1_SCORE += b.winning_score(board, b.PLAYER_PIECE)
                        AI2_SCORE += b.winning_score(board, b.AI_PIECE)
                        game_over = True

                    global deptho2
                    root2 = Node(board)
                    start_time = time.time()
                    col, minimax_scorecore = mai.min_max_Function(board, deptho2, AI2, -math.inf, math.inf, root2,algorithmChoice2)
                    end_time = time.time()
                    print(
                        "time taken = " + str(end_time - start_time))  # calculate time taked and display it in console


                    if b.is_valid_location(board, col):
                        # pygame.time.wait(500)
                        row = b.get_next_open_row(board, col)
                        b.drop_piece(board, row, col, b.AI_PIECE)

                        b.draw_board(board)
                        root2.name = str(minimax_scorecore) + "\n" + str(np.flip(board, 0))
                        # DotExporter(root).to_picture("udo.svg") #comment this line when we attempt depth more than 4
                        # os.system('udo.svg')
                        print("Nodes explored " + str(mai.count))
                        # print("leaf nodes  " + str(mai.leafs))
                        mai.count = 0
                        mai.counter=0
                        mai.leafs=0
                        turn += 1
                        turn = turn % 2
                        if b.is_terminal_node(board):
                            AI1_SCORE += b.winning_score(board, b.PLAYER_PIECE)
                            AI2_SCORE += b.winning_score(board, b.AI_PIECE)
                            turn=-1
                            game_over=True

    print("AI1 score is = " + str(AI1_SCORE))
    print("AI2 score is = " + str(AI2_SCORE))
    if AI1_SCORE<AI2_SCORE:
        print("winner is AI 2")
    elif AI1_SCORE>AI2_SCORE:
        print("winner is AI 1")
    else:
        print("draw")
    time.sleep(5)
    exit()


def start():
    global turn
    board = b.create_board()
    b.print_board(board)
    game_over = False
    PLAYER = 0
    AI = 1
    AI_SCORE = 0
    PLAYER_SCORE = 0
    screen = pygame.display.set_mode(b.size)
    b.draw_board(board)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, b.width, b.SQUARESIZE))  # to clear circles
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(b.SQUARESIZE / 2)), b.RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, b.width, b.SQUARESIZE))
                # Ask for Player 1 Input
                if turn == PLAYER:

                    posx = event.pos[0]
                    col = int(math.floor(posx / b.SQUARESIZE))

                    if b.is_valid_location(board, col):
                        row = b.get_next_open_row(board, col)
                        b.drop_piece(board, row, col, b.PLAYER_PIECE)
                        turn += 1
                        turn = turn % 2

                    if b.is_terminal_node(board):
                        AI_SCORE += b.winning_score(board, b.AI_PIECE)
                        PLAYER_SCORE += b.winning_score(board, b.PLAYER_PIECE)
                        game_over = True

                b.draw_board(board)

                if turn == AI and not game_over:
                    if b.is_terminal_node(board):
                        AI_SCORE += b.winning_score(board, b.AI_PIECE)
                        PLAYER_SCORE += b.winning_score(board, b.PLAYER_PIECE)
                        game_over = True

                    global deptho
                    root = Node(board)
                    start_time = time.time()
                    col, minimax_scorecore = mi.min_max_Function(board, deptho, AI, -math.inf, math.inf, root,algorithmChoice)
                    end_time = time.time()
                    print(
                        "time taken = " + str(end_time - start_time))  # calculate time taked and display it in console

                    if b.is_valid_location(board, col):
                        # pygame.time.wait(500)
                        row = b.get_next_open_row(board, col)
                        b.drop_piece(board, row, col, b.AI_PIECE)

                        b.draw_board(board)
                        root.name = str(minimax_scorecore) + "\n" + str(np.flip(board, 0))
                        print("Nodes explored " + str(mi.count))
                        # print("leaf nodes  " + str(mi.leafs))
                        mi.count=0
                        mi.counter=0
                        mi.leafs=0
                        turn += 1
                        turn = turn % 2

    print("AI score is = " + str(AI_SCORE))
    print("Player score is = " + str(PLAYER_SCORE))
    if AI_SCORE<PLAYER_SCORE:
        print("winner is player")
    elif AI_SCORE>PLAYER_SCORE:
        print("winner is AI")
    else:
        print("draw")
    time.sleep(5)
    exit()

def button(screen, position, text, color=(100, 100, 100)):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 255, 255))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, color, (x, y, w, h))
    return screen.blit(text_render, (x, y))


def menu():
    """ This is the menu that waits you to click the s key to start """
    global turn
    global deptho1
    global deptho2
    colorAI = (100, 100, 100)
    colorPlayer = (100, 100, 100)
    colorPruning = (100, 100, 100)
    colorNoPruning = (100, 100, 100)
    b1 = button(screen1, (150, 150), "PLAYER  VS   AI  ", colorPlayer)
    b2 = button(screen1, (180, 325), "  AI    VS   AI  ", (100, 100, 100))
    b3 = button(screen1, (188, 500), "       Quit      ")
    font = pygame.font.SysFont("Arial", 50)
    text = font.render('  WELCOME to our connect 4', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (600 // 2, 50)
    turnCheck = 0
    algoCheck = 0
    depthCheck = 0
    clock = pygame.time.Clock()
    while True:
        screen1.blit(text, textRect)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.display.flip()
                    screen1.fill((0,0,0))
                    menuplayer()

                elif b2.collidepoint(pygame.mouse.get_pos()):
                    pygame.display.flip()
                    screen1.fill((0,0,0))
                    menuai()

                elif b3.collidepoint(pygame.mouse.get_pos()):
                    exit()

        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()
    pygame.quit()


def menuai():
    """ This is the menu that waits you to click the s key to start """
    global turn
    global deptho1
    global deptho2
    global algorithmChoice1
    global algorithmChoice2
    colorAI = (100, 100, 100)
    colorPlayer = (100, 100, 100)
    colorPruning = (100, 100, 100)
    colorNoPruning = (100, 100, 100)
    b1 = button(screen3, (170, 500), "Quit")
    b2 = button(screen3, (570, 500), "Start")
    b3 = button(screen3, (570, 150), "AI  2", colorAI)
    b4 = button(screen3, (170, 150), "AI  1", colorPlayer)
    b51 = button(screen3, (50, 300), "Pruning", colorPruning)
    b61 = button(screen3, (250, 300), "without", colorNoPruning)
    b52 = button(screen3, (450, 300), "Pruning", colorPruning)
    b62 = button(screen3, (650, 300), "without", colorNoPruning)
    b71 = button(screen3, (300, 390), "Enter", (100, 100, 100))
    b72 = button(screen3, (700, 390), "Enter", (100, 100, 100))
    font = pygame.font.SysFont("Arial", 50)
    font1 = pygame.font.SysFont("Arial", 32)
    text = font.render('                        Please select the first player', True, (255, 255, 255))
    text1 = font1.render('Depth 1', True, (255, 255, 255))
    text2 = font1.render('Depth 2', True, (255, 255, 255))
    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()
    textRect = text.get_rect()
    textRect1.center = (70, 410)
    textRect2.center = (470, 410)
    textRect.center = (600 // 2, 50)
    turnCheck = 0
    algoCheck = 0
    depthCheck = 0
    clock = pygame.time.Clock()
    # it will display on screen
    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text1 = ''
    user_text2 = ''
    input_rect1 = pygame.Rect(150, 400, 140, 32)
    input_rect2 = pygame.Rect(550, 400, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active1 = False
    active2 = False
    while True:
        screen3.blit(text, textRect)
        screen3.blit(text1, textRect1)
        screen3.blit(text2, textRect2)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    exit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    if turnCheck == 0 and algoCheck == 0 and depthCheck == 0:
                        ctypes.windll.user32.MessageBoxW(0, "Please algo & depth", "ERROR!", 1)
                    else:
                        pygame.display.flip()
                        startai()
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    turn = 1
                    turnCheck = 1
                    colorAI = (0, 0, 100)
                    colorPlayer = (100, 100, 100)
                    b3 = button(screen3, (570, 150), "AI  2", colorAI)
                    b4 = button(screen3, (170, 150), "AI  1", colorPlayer)
                elif b4.collidepoint(pygame.mouse.get_pos()):
                    turn = 0
                    turnCheck = 1
                    colorAI = (100, 100, 100)
                    colorPlayer = (0, 0, 100)
                    b3 = button(screen3, (570, 150), "AI  2", colorAI)
                    b4 = button(screen3, (170, 150), "AI  1", colorPlayer)
                elif b51.collidepoint(pygame.mouse.get_pos()):
                    algorithmChoice1 = 0
                    algoCheck = 1
                    colorPruning = (0, 0, 100)
                    colorNoPruning = (100, 100, 100)
                    b51 = button(screen3, (50, 300), "Pruning", colorPruning)
                    b61 = button(screen3, (250, 300), "without", colorNoPruning)
                elif b52.collidepoint(pygame.mouse.get_pos()):
                    algorithmChoice2 = 0
                    algoCheck = 1
                    colorPruning = (0, 0, 100)
                    colorNoPruning = (100, 100, 100)
                    b52 = button(screen3, (450, 300), "Pruning", colorPruning)
                    b62 = button(screen3, (650, 300), "without", colorNoPruning)
                elif b61.collidepoint(pygame.mouse.get_pos()):
                    algorithmChoice1 = 1
                    algoCheck = 1
                    colorPruning = (100, 100, 100)
                    colorNoPruning = (0, 0, 100)
                    b51 = button(screen3, (50, 300), "Pruning", colorPruning)
                    b61 = button(screen3, (250, 300), "without", colorNoPruning)
                elif b62.collidepoint(pygame.mouse.get_pos()):
                    algorithmChoice2 = 1
                    algoCheck = 1
                    colorPruning = (100, 100, 100)
                    colorNoPruning = (0, 0, 100)
                    b52 = button(screen3, (450, 300), "Pruning", colorPruning)
                    b62 = button(screen3, (650, 300), "without", colorNoPruning)
                elif b71.collidepoint(pygame.mouse.get_pos()):
                    depthCheck = 1
                    deptho1 = int(user_text1)
                    print('depth 1 is'+str(deptho1))
                elif b72.collidepoint(pygame.mouse.get_pos()):
                    depthCheck = 1
                    deptho2 = int(user_text2)
                    print('depth 2 is'+str(deptho2))
                if input_rect1.collidepoint(event.pos):
                    active1 = True
                else:
                    active1 = False
                if input_rect2.collidepoint(event.pos):
                    active2 = True
                else:
                    active2 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text1 = user_text1[:-1]
                else:
                    user_text1 += event.unicode
                if event.key == pygame.K_RETURN:
                    deptho1 = int(user_text1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text2 = user_text2[:-1]
                else:
                    user_text2 += event.unicode
                if event.key == pygame.K_RETURN:
                    deptho2 = int(user_text2)
        if active1:
            color = color_active
        else:
            color = color_passive
        if active2:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen3, color, input_rect1)
        pygame.draw.rect(screen3, color, input_rect2)

        text_surface1 = base_font.render(user_text1, True, (255, 255, 255))
        text_surface2 = base_font.render(user_text2, True, (255, 255, 255))
        screen3.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        screen3.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
        input_rect1.w = max(100, text_surface1.get_width() + 10)
        input_rect2.w = max(100, text_surface2.get_width() + 10)
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()
    pygame.quit()


def menuplayer():
    """ This is the menu that waits you to click the s key to start """
    global turn
    global deptho
    global algorithmChoice
    colorAI = (100, 100, 100)
    colorPlayer = (100, 100, 100)
    colorPruning = (100, 100, 100)
    colorNoPruning = (100, 100, 100)
    b1 = button(screen2, (150, 500), "Quit")
    b2 = button(screen2, (400, 500), "Start")
    b3 = button(screen2, (400, 150), "AI", colorAI)
    b4 = button(screen2, (150, 150), "Player", colorPlayer)
    b5 = button(screen2, (150, 300), "Pruning", colorPruning)
    b6 = button(screen2, (400, 300), "without", colorNoPruning)
    b7 = button(screen2, (520, 390), "Enter", (100, 100, 100))
    font = pygame.font.SysFont("Arial", 50)
    font1 = pygame.font.SysFont("Arial", 32)
    text = font.render('       Please select the first player', True, (255, 255, 255))
    text1 = font1.render('Depth', True, (255, 255, 255))
    textRect1 = text1.get_rect()
    textRect = text.get_rect()
    textRect1.center = (250, 410)
    textRect.center = (600 // 2, 50)
    turnCheck = 0
    algoCheck = 0
    depthCheck = 0
    clock = pygame.time.Clock()
    # it will display on screen
    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(350, 400, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active = False

    while True:
        screen2.blit(text, textRect)
        screen2.blit(text1, textRect1)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    exit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    if turnCheck == 0 and algoCheck == 0 and depthCheck == 0:
                        ctypes.windll.user32.MessageBoxW(0, "Please select who will play first", "ERROR!", 1)
                    else:
                        pygame.display.flip()
                        start()
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    turn = 1
                    turnCheck = 1
                    colorAI = (0, 0, 100)
                    colorPlayer = (100, 100, 100)
                    b3 = button(screen2, (400, 150), "AI", colorAI)
                    b4 = button(screen2, (150, 150), "Player", colorPlayer)
                elif b4.collidepoint(pygame.mouse.get_pos()):
                    turn = 0
                    turnCheck = 1
                    colorAI = (100, 100, 100)
                    colorPlayer = (0, 0, 100)
                    b3 = button(screen2, (400, 150), "AI", colorAI)
                    b4 = button(screen2, (150, 150), "Player", colorPlayer)
                elif b5.collidepoint(pygame.mouse.get_pos()):
                    algorithmChoice = 0
                    algoCheck = 1
                    colorPruning = (0, 0, 100)
                    colorNoPruning = (100, 100, 100)
                    b5 = button(screen2, (150, 300), "Pruning", colorPruning)
                    b6 = button(screen2, (400, 300), "without", colorNoPruning)
                elif b6.collidepoint(pygame.mouse.get_pos()):
                    algorithmChoice = 1
                    algoCheck = 1
                    colorPruning = (100, 100, 100)
                    colorNoPruning = (0, 0, 100)
                    b5 = button(screen2, (150, 300), "Pruning", colorPruning)
                    b6 = button(screen2, (400, 300), "without", colorNoPruning)
                elif b7.collidepoint(pygame.mouse.get_pos()):
                    depthCheck = 1
                    deptho = int(user_text)
                    print(deptho)
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                if event.key == pygame.K_RETURN:
                    deptho = int(user_text)
        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen2, color, input_rect)

        text_surface = base_font.render(user_text, True, (255, 255, 255))

        screen2.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()
    pygame.quit()


menu()
