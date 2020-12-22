import numpy as np
import sys
import math
import random
import pygame


# Global variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

NUM_1 = "1"
NUM_2 = "2"
NUM_3 = "3"
NUM_4 = "4"
NUM_5 = "5"
NUM_6 = "6"
NUM_7 = "7"
NUM_8 = "8"
NUM_9 = "9"
NUM_0 = "0"

ground = np.array([[7, 1, 9, 8, 3, 6, 5, 4, 2],
                   [3, 2, 8, 5, 1, 4, 9, 7, 6],
                   [6, 5, 4, 9, 7, 2, 1, 8, 3],
                   [4, 8, 1, 6, 9, 5, 2, 3, 7],
                   [9, 6, 3, 7, 2, 1, 8, 5, 4],
                   [2, 7, 5, 4, 8, 3, 6, 9, 1],
                   [8, 3, 7, 1, 6, 9, 4, 2, 5],
                   [5, 9, 6, 2, 4, 7, 3, 1, 8],
                   [1, 4, 2, 3, 5, 8, 7, 6, 9]], dtype=int)
playboard = np.array([[7, 0, 0, 8, 3, 6, 5, 4, 2],
                      [3, 0, 0, 0, 1, 0, 9, 0, 0],
                      [6, 5, 4, 0, 0, 0, 0, 8, 0],
                      [0, 0, 1, 0, 9, 0, 0, 0, 0],
                      [0, 6, 0, 0, 2, 0, 8, 0, 0],
                      [0, 0, 5, 0, 8, 0, 6, 0, 0],
                      [0, 3, 0, 1, 6, 0, 0, 2, 0],
                      [0, 9, 6, 0, 4, 0, 0, 1, 8],
                      [0, 4, 0, 3, 5, 8, 7, 0, 0]], dtype=int)
x = np.zeros((9, 9), dtype=int)
for i in range(9):
    for j in range(9):
        if playboard[i][j] == 0:
            x[i][j] = 1


# Functions
def draw_grid():
    for line in range(10):
        pygame.draw.line(win, BLACK, (0 + line * 30, 0), (0 + line * 30, 271))
        pygame.draw.line(win, BLACK, (0, 0 + line * 30), (271, 0 + line * 30))
    for line in range(4):
        pygame.draw.line(win, BLACK, (0 + line * 90, 0), (0 + line*90, 271), 3)
        pygame.draw.line(win, BLACK, (0, 0 + line * 90), (271, 0 + line*90), 3)


def select():
    if col < 9 and row < 9:
        pygame.draw.rect(win, BLUE, (col * 30, row * 30, 30, 30))


def draw_num():
    for i in range(9):
        for j in range(9):
            if playboard[j][i] == 1:
                label = my_font.render(NUM_1, 1, BLACK)
                win.blit(label, (i * 30 + 10, j * 30))
            if playboard[j][i] == 2:
                label = my_font.render(NUM_2, 1, BLACK)
                win.blit(label, (i * 30 + 10, j * 30))
            if playboard[j][i] == 3:
                label = my_font.render(NUM_3, 1, BLACK)
                win.blit(label, (i * 30 + 10, j * 30))
            if playboard[j][i] == 4:
                label = my_font.render(NUM_4, 1, BLACK)
                win.blit(label, (i * 30 + 10, j * 30))
            if playboard[j][i] == 5:
                label = my_font.render(NUM_5, 1, BLACK)
                win.blit(label, (i * 30 + 10, j * 30))
            if playboard[j][i] == 6:
                label = my_font.render(NUM_6, 1, BLACK)
                win.blit(label, (i * 30 + 10, j * 30))
            if playboard[j][i] == 7:
                label = my_font.render(NUM_7, 1, BLACK)
                win.blit(label, (i * 30 + 10, j * 30))
            if playboard[j][i] == 8:
                label = my_font.render(NUM_8, 1, BLACK)
                win.blit(label, (i * 30 + 10, j * 30))
            if playboard[j][i] == 9:
                label = my_font.render(NUM_9, 1, BLACK)
                win.blit(label, (i * 30 + 10, j * 30))
            if playboard[j][i] == 0:
                pass


def insertNum(mistake):
    if playboard[row][col] == 0:
        if event.key == pygame.K_1:
            playboard[row][col] = 1
        if event.key == pygame.K_2:
            playboard[row][col] = 2
        if event.key == pygame.K_3:
            playboard[row][col] = 3
        if event.key == pygame.K_4:
            playboard[row][col] = 4
        if event.key == pygame.K_5:
            playboard[row][col] = 5
        if event.key == pygame.K_6:
            playboard[row][col] = 6
        if event.key == pygame.K_7:
            playboard[row][col] = 7
        if event.key == pygame.K_8:
            playboard[row][col] = 8
        if event.key == pygame.K_9:
            playboard[row][col] = 9
    if playboard[row][col] != 0:
        if playboard[row][col] != ground[row][col]:
            mistake += 1
    if playboard[row][col] == ground[row][col]:
        x[row][col] = 0
    return mistake


def check():
    count = 0
    for i in range(9):
        for j in range(9):
            if x[i][j] == 0:
                count += 1
    if count == 81:
        return True
    else:
        return False


def score(mistake, game):
    if not game:
        label = text.render(f"Mistake: {mistake}", 1, BLACK)
        win.blit(label, (50, 280))
    else:
        label = text.render("Game Over", 1, BLACK)
        win.blit(label, (30, 271))
        label = my_font.render(f"Mistakes {mistake}", 1, BLACK)
        win.blit(label, (30, 320))


# Local variables
mistake = 0
row, row = [0, 0]
selected = False
board = np.zeros((9, 9))
# board = shuffle_board(board)

# Game setup
pygame.init()
win = pygame.display.set_mode((271, 350))
pygame.display.set_caption("SUDOKU")
my_font = pygame.font.SysFont("arial", 25)
text = pygame.font.SysFont("arial", 50)
play = True
game = False

# Main loop
while play:
    pygame.time.delay(70)
    win.fill(WHITE)
    draw_grid()
    score(mistake, game)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor_pos = event.pos
            col = math.floor(cursor_pos[0] / 30)
            row = math.floor(cursor_pos[1] / 30)
            selected = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if x[row][col] == 1:
                    playboard[row][col] = 0
            mistake = insertNum(mistake)
    if selected:
        select()
    draw_num()
    game = check()
    if game:
        pass
    else:
        count = 0
    pygame.display.update()
