import pygame
import numpy as np

pygame.init()

Width = 600
Height = 600
bg_color = (28, 170, 156)
line_lenght = 15
line_color = (23, 145, 135)
pos_Y = 0
pos_X = 0

screen = pygame.display.set_mode( (Width, Height) )
pygame.display.set_caption("tic tac toe")
screen.fill( bg_color )
def draw_line():
    pygame.draw.line(screen, line_color, (200, 0), (200, 600), line_lenght)
    pygame.draw.line(screen, line_color, (400, 0), (400, 600), line_lenght)
    pygame.draw.line(screen, line_color, (0, 200), (600, 200), line_lenght)
    pygame.draw.line(screen, line_color, (0, 400), (600, 400), line_lenght)

board = np.zeros( (3, 3) )

def mark_square(row, col, player):
    board[row][col] = player

def square_available(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def is_full():
    for col in board:
        for row in col:
            if board[col][row] == 0:
                return False
    return True    

def draw_figures():
    for col in range(3):
        for row in range(3):
            if board[col][row] == 1:
                pygame.draw.line(screen, line_color, ( (row * 200) + 30 , (col * 200) + 30 ), ( (row * 200 + 200) - 30 , (col * 200 + 200) - 30 ), line_lenght)
                pygame.draw.line(screen, line_color, ( (row * 200 + 200) - 30 , (col * 200) + 30 ), ( (row * 200) + 30, (col * 200 + 200) - 30 ), line_lenght)
            elif board[col][row] == 2:
                pygame.draw.circle(screen, line_color, ( row * 200 + 200 / 2, col * 200 + 200 / 2 ), 60, line_lenght)

def check_win(player):
    for col in range(3):
        if board[col][0] == player and board[col][1] == player and board[col][2] == player:
            draw_vertical(col, player)
            return True
    for row in range(3):
        if board[0][row] == player and board[1][row] == player and board[2][row] == player:
            draw_horizontal(row, player)
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc(player)
        return True
    
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc(player)
        return True
    
    return False

                
def draw_vertical(col, player):

    pos_Y = col * 200 + 100

    if player == 1:
        win_color = (0, 0, 0)
    elif player == 2:
        win_color = (255, 255, 255)

    pygame.draw.line(screen, win_color, (0, pos_Y), (600, pos_Y), line_lenght)
    


def draw_horizontal(row, player):
    pos_X = row * 200 + 100
    
    if player == 1:
        win_color = (0, 0, 0)
    elif player == 2:
        win_color = (255, 255, 255)

    pygame.draw.line(screen, win_color, (pos_X, 0), (pos_X, 600), line_lenght)

def draw_desc(player):
    if player == 1:
        win_color = (0, 0, 0)
    elif player == 2:
        win_color = (255, 255, 255)

    pygame.draw.line(screen, win_color, (10, 10), (590, 590), line_lenght)

def draw_asc(player):
    if player == 1:
        win_color = (0, 0, 0)
    elif player == 2:
        win_color = (255, 255, 255)

    pygame.draw.line(screen, win_color, (10, 590), (590, 10), line_lenght)




is_true = True


draw_line()
is_over = False


def restart():
    screen.fill( bg_color )
    draw_line()
    for col in range(3):
        for row in range(3):
            board[col][row] = 0
player = 1

while is_true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_true = False

        if event.type == pygame.MOUSEBUTTONDOWN and not is_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            posX = int(mouseX // 200)
            posY = int(mouseY // 200)
            if square_available(posY, posX):
                if player == 1:
                    mark_square(posY, posX, player)
                    draw_figures()
                    if check_win(player):
                        is_over = True
                    player = 2
                elif player == 2:
                    mark_square(posY, posX, player)
                    draw_figures()
                    if check_win(player):
                        is_over = True
                    player = 1
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                restart()
                is_over = False

    pygame.display.update()
