import numpy as np
import pygame
import sys
import math
import alpha

ROW_COUNT = 6
COLUMN_COUNT = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
RADIUS = int(50 - 5)


def create_board():
    board_first = np.zeros((6, 7))
    return board_first


def drop_piece(board_, row_, col_, piece):
    board_[row_][col_] = piece


def is_valid_location(board_, col_):
    return board_[ROW_COUNT - 1][col_] == 0


def get_next_open_row(board_, col_):
    for r in range(ROW_COUNT):
        if board_[r][col_] == 0:
            return r


def print_board(board_):
    print(np.flip(board_, 0))


def winning_move(board_, piece):
    # Horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board_[r][c] == piece and board[r][c + 1] == piece and board_[r][c + 2] == piece and \
                    board_[r][c + 3] == piece:
                return True
    # Vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and \
                    board[r + 3][c] == piece:
                return True
    # Diagonal up
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                    board[r + 3][c + 3] == piece:
                return True
    # Diagonal down
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                    board[r - 3][c + 3] == piece:
                return True


def draw_board(board_):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                               int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board_[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                 height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board_[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                    height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

# PyGame start point ---------------------------------------------------------------------------------------------------
pygame.init()

SQUARE_SIZE = 100

width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

my_font = pygame.font.SysFont(alpha.Fonts.font1, 75)

while not game_over:
    # Ask for PLayer 1 input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            pos_x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))

            if turn == 0:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / SQUARE_SIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = my_font.render("Player 1 Wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
            else:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / SQUARE_SIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = my_font.render("Player 2 Wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True
            print_board(board)
            draw_board(board)
            turn += 1
            turn %= 2

            if game_over:
                pygame.time.wait(1500)
                game_over = False
                board = create_board()
                draw_board(board)
                pygame.display.update()
