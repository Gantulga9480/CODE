import numpy as np
import pygame
import math
import sys

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
SQUARE_SIZE = 100


def draw_line():
    for ite in range(4):
        pygame.draw.line(win, WHITE, (0 + ite * 100, 0), (0 + ite * 100, 300))
        pygame.draw.line(win, WHITE, (0, 0 + ite * 100), (300, 0 + ite * 100))


def draw_tic_tac(shape_, pos_):
    for x in shape_:
        for items in pos_:
            for item in items:
                if x[0] and x[0][1] == 0 and not item:
                    pygame.draw.line(win, RED, (20 + x[1][0] * SQUARE_SIZE, 20 + x[1][1] * SQUARE_SIZE),
                                     (80 + x[1][0] * SQUARE_SIZE, 80 + x[1][1] * SQUARE_SIZE), 5)
                    pygame.draw.line(win, RED, (80 + x[1][0] * SQUARE_SIZE, 20 + x[1][1] * SQUARE_SIZE),
                                     (20 + x[1][0] * SQUARE_SIZE, 80 + x[1][1] * SQUARE_SIZE), 5)
                elif x[0] and x[0][1] == 1 and not item:
                    pygame.draw.circle(win, BLUE, (50 + x[1][0] * SQUARE_SIZE, 50 + x[1][1] * SQUARE_SIZE), 30)


def draw_shape(columns, rows, turn_, board_, pos_, duplicate_):
    abc = turn_
    if turn_ == 0:
        abc = 1
    elif turn_ == 1:
        abc = 2
    if columns == 0 and rows == 0:
        duplicate_[0] += 1
        if duplicate_[0] > 1:
            pos_[rows][columns] = True
        elif duplicate_[0] == 1:
            board_[0][0] = abc
            shape[0] = [(True, turn_), (columns, rows)]
    elif columns == 1 and rows == 0:
        duplicate_[1] += 1
        if duplicate_[1] > 1:
            pos_[rows][columns] = True
        elif duplicate_[1] == 1:
            board_[0][1] = abc
            shape[1] = [(True, turn_), (columns, rows)]
    elif columns == 2 and rows == 0:
        duplicate_[2] += 1
        if duplicate_[2] > 1:
            pos_[rows][columns] = True
        elif duplicate_[2] == 1:
            board_[0][2] = abc
            shape[2] = [(True, turn_), (columns, rows)]
    elif columns == 0 and rows == 1:
        duplicate_[3] += 1
        if duplicate_[3] > 1:
            pos_[rows][columns] = True
        elif duplicate_[3] == 1:
            board_[1][0] = abc
            shape[3] = [(True, turn_), (columns, rows)]
    elif columns == 1 and rows == 1:
        duplicate_[4] += 1
        if duplicate_[4] > 1:
            pos_[rows][columns] = True
        elif duplicate_[4] == 1:
            board_[1][1] = abc
            shape[4] = [(True, turn_), (columns, rows)]
    elif columns == 2 and rows == 1:
        duplicate_[5] += 1
        if duplicate_[5] > 1:
            pos_[rows][columns] = True
        elif duplicate_[5] == 1:
            board_[1][2] = abc
            shape[5] = [(True, turn_), (columns, rows)]
    elif columns == 0 and rows == 2:
        duplicate_[6] += 1
        if duplicate_[6] > 1:
            pos_[rows][columns] = True
        elif duplicate_[6] == 1:
            board_[2][0] = abc
            shape[6] = [(True, turn_), (columns, rows)]
    elif columns == 1 and rows == 2:
        duplicate_[7] += 1
        if duplicate_[7] > 1:
            pos_[rows][columns] = True
        elif duplicate_[7] == 1:
            board_[2][1] = abc
            shape[7] = [(True, turn_), (columns, rows)]
    elif columns == 2 and rows == 2:
        duplicate_[8] += 1
        if duplicate_[8] > 1:
            pos_[rows][columns] = True
        elif duplicate_[8] == 1:
            board_[2][2] = abc
            shape[8] = [(True, turn_), (columns, rows)]
    return shape, board_, pos_, duplicate_


def check_win(board_):
    if board_[0][0] == 1 and board_[1][1] == 1 and board_[2][2] == 1:
        return False
    elif board_[0][2] == 1 and board_[1][1] == 1 and board_[2][0] == 1:
        return False
    elif board_[0][0] == 1 and board_[1][0] == 1 and board_[2][0] == 1:
        return False
    elif board_[0][1] == 1 and board_[1][1] == 1 and board_[2][1] == 1:
        return False
    elif board_[0][2] == 1 and board_[1][2] == 1 and board_[2][2] == 1:
        return False
    elif board_[0][0] == 1 and board_[0][1] == 1 and board_[0][2] == 1:
        return False
    elif board_[1][0] == 1 and board_[1][1] == 1 and board_[1][2] == 1:
        return False
    elif board_[2][0] == 1 and board_[2][1] == 1 and board_[2][2] == 1:
        return False
    elif board_[0][0] == 2 and board_[1][1] == 2 and board_[2][2] == 2:
        return False
    elif board_[0][2] == 2 and board_[1][1] == 2 and board_[2][0] == 2:
        return False
    elif board_[0][0] == 2 and board_[1][0] == 2 and board_[2][0] == 2:
        return False
    elif board_[0][1] == 2 and board_[1][1] == 2 and board_[2][1] == 2:
        return False
    elif board_[0][2] == 2 and board_[1][2] == 2 and board_[2][2] == 2:
        return False
    elif board_[0][0] == 2 and board_[0][1] == 2 and board_[0][2] == 2:
        return False
    elif board_[1][0] == 2 and board_[1][1] == 2 and board_[1][2] == 2:
        return False
    elif board_[2][0] == 2 and board_[2][1] == 2 and board_[2][2] == 2:
        return False
    else:
        return True


def restart():
    board_ = np.zeros((3, 3))
    col_ = 10
    row_ = 10
    pos_ = [[False, False, False],
            [False, False, False],
            [False, False, False]]
    shape_ = [[False, (0, 0)], [False, (0, 0)], [False, (0, 0)],
              [False, (0, 0)], [False, (0, 0)], [False, (0, 0)],
              [False, (0, 0)], [False, (0, 0)], [False, (0, 0)]]
    duplicate_ = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    return board_, shape_, col_, row_, pos_, duplicate_


turn = 0
duplicate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
shape = [[False, (0, 0)], [False, (0, 0)], [False, (0, 0)],
         [False, (0, 0)], [False, (0, 0)], [False, (0, 0)],
         [False, (0, 0)], [False, (0, 0)], [False, (0, 0)]]
col = 10
row = 10
board = np.zeros((3, 3))
pos = [[False, False, False],
       [False, False, False],
       [False, False, False]]
pygame.init()
win = pygame.display.set_mode((301, 301))
pygame.display.set_caption("Tic Tac Toe")
run = True
while run:
    pygame.time.delay(10)
    a = 0
    win.fill((129, 129, 129))
    draw_line()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor_pos = event.__pos
            turn += 3
            turn %= 2
            col = math.floor(cursor_pos[0] / SQUARE_SIZE)
            row = math.floor(cursor_pos[1] / SQUARE_SIZE)
    shape, board, pos, duplicate = draw_shape(col, row, turn, board, pos, duplicate)
    draw_tic_tac(shape, pos)
    pygame.display.update()
    run = check_win(board)
    for it in pos:
        for q in it:
            if q:
                a += 1
            else:
                pass
    if not run or a == 9:
        board, shape, col, row, pos, duplicate = restart()
        pygame.time.delay(1000)
        run = True
    else:
        pass
