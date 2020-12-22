import numpy as np
import pygame
import math
import sys
import alpha

SQUARE_SIZE = 100


class Draw:

    def __init__(self, background):
        self.__back = background

    def _draw_line(self):
        for ite in range(4):
            pygame.draw.line(win, self.__back, (0 + ite * 100, 0), (0 + ite * 100, 300))
            pygame.draw.line(win, self.__back, (0, 0 + ite * 100), (300, 0 + ite * 100))


class TicTacToe(Draw):

    def __init__(self, background):
        super().__init__(background)
        self.__background = background

        self.__pos = [[False, False, False],
                      [False, False, False],
                      [False, False, False]]
        self.__shape = [[False, (0, 0)], [False, (0, 0)], [False, (0, 0)],
                        [False, (0, 0)], [False, (0, 0)], [False, (0, 0)],
                        [False, (0, 0)], [False, (0, 0)], [False, (0, 0)]]
        self.__duplicate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__turn = 0
        self.__col = 10
        self.__row = 10
        self.__board = np.zeros((3, 3))

    def draw_tic_tac(self):
        for x in self.__shape:
            for items in self.__pos:
                for item in items:
                    if x[0] and x[0][1] == 0 and not item:
                        pygame.draw.line(win, alpha.Colors.RED, (20 + x[1][0] * SQUARE_SIZE, 20 + x[1][1] *
                                                                 SQUARE_SIZE),
                                         (80 + x[1][0] * SQUARE_SIZE, 80 + x[1][1] * SQUARE_SIZE), 5)
                        pygame.draw.line(win, alpha.Colors.RED, (80 + x[1][0] * SQUARE_SIZE, 20 + x[1][1] *
                                                                 SQUARE_SIZE),
                                         (20 + x[1][0] * SQUARE_SIZE, 80 + x[1][1] * SQUARE_SIZE), 5)
                    elif x[0] and x[0][1] == 1 and not item:
                        pygame.draw.circle(win, self.__background, (50 + x[1][0] * SQUARE_SIZE, 50 + x[1][1] *
                                                                    SQUARE_SIZE), 30)

    def draw_shape(self):
        if self.__col == 0 and self.__row == 0:
            self.__duplicate[0] += 1
            if self.__duplicate[0] > 1:
                self.__pos[self.__row][self.__col] = True
            elif self.__duplicate[0] == 1:
                self.__board[0][0] = self.__turn + 1
                self.__shape[0] = [(True, self.__turn), (self.__col, self.__row)]
        elif self.__col == 1 and self.__row == 0:
            self.__duplicate[1] += 1
            if self.__duplicate[1] > 1:
                self.__pos[self.__row][self.__col] = True
            elif self.__duplicate[1] == 1:
                self.__board[0][1] = self.__turn + 1
                self.__shape[1] = [(True, self.__turn), (self.__col, self.__row)]
        elif self.__col == 2 and self.__row == 0:
            self.__duplicate[2] += 1
            if self.__duplicate[2] > 1:
                self.__pos[self.__row][self.__col] = True
            elif self.__duplicate[2] == 1:
                self.__board[0][2] = self.__turn + 1
                self.__shape[2] = [(True, self.__turn), (self.__col, self.__row)]
        elif self.__col == 0 and self.__row == 1:
            self.__duplicate[3] += 1
            if self.__duplicate[3] > 1:
                self.__pos[self.__row][self.__col] = True
            elif self.__duplicate[3] == 1:
                self.__board[1][0] = self.__turn + 1
                self.__shape[3] = [(True, self.__turn), (self.__col, self.__row)]
        elif self.__col == 1 and self.__row == 1:
            self.__duplicate[4] += 1
            if self.__duplicate[4] > 1:
                self.__pos[self.__row][self.__col] = True
            elif self.__duplicate[4] == 1:
                self.__board[1][1] = self.__turn + 1
                self.__shape[4] = [(True, self.__turn), (self.__col, self.__row)]
        elif self.__col == 2 and self.__row == 1:
            self.__duplicate[5] += 1
            if self.__duplicate[5] > 1:
                self.__pos[self.__row][self.__col] = True
            elif self.__duplicate[5] == 1:
                self.__board[1][2] = self.__turn + 1
                self.__shape[5] = [(True, self.__turn), (self.__col, self.__row)]
        elif self.__col == 0 and self.__row == 2:
            self.__duplicate[6] += 1
            if self.__duplicate[6] > 1:
                self.__pos[self.__row][self.__col] = True
            elif self.__duplicate[6] == 1:
                self.__board[2][0] = self.__turn + 1
                self.__shape[6] = [(True, self.__turn), (self.__col, self.__row)]
        elif self.__col == 1 and self.__row == 2:
            self.__duplicate[7] += 1
            if self.__duplicate[7] > 1:
                self.__pos[self.__row][self.__col] = True
            elif self.__duplicate[7] == 1:
                self.__board[2][1] = self.__turn + 1
                self.__shape[7] = [(True, self.__turn), (self.__col, self.__row)]
        elif self.__col == 2 and self.__row == 2:
            self.__duplicate[8] += 1
            if self.__duplicate[8] > 1:
                self.__pos[self.__row][self.__col] = True
            elif self.__duplicate[8] == 1:
                self.__board[2][2] = self.__turn + 1
                self.__shape[8] = [(True, self.__turn), (self.__col, self.__row)]

    def sel_turn(self):
        self.__turn += 3
        self.__turn %= 2

    def check_win(self):
        if self.__board[0][0] == 1 and self.__board[1][1] == 1 and self.__board[2][2] == 1:
            return False
        elif self.__board[0][2] == 1 and self.__board[1][1] == 1 and self.__board[2][0] == 1:
            return False
        elif self.__board[0][0] == 1 and self.__board[1][0] == 1 and self.__board[2][0] == 1:
            return False
        elif self.__board[0][1] == 1 and self.__board[1][1] == 1 and self.__board[2][1] == 1:
            return False
        elif self.__board[0][2] == 1 and self.__board[1][2] == 1 and self.__board[2][2] == 1:
            return False
        elif self.__board[0][0] == 1 and self.__board[0][1] == 1 and self.__board[0][2] == 1:
            return False
        elif self.__board[1][0] == 1 and self.__board[1][1] == 1 and self.__board[1][2] == 1:
            return False
        elif self.__board[2][0] == 1 and self.__board[2][1] == 1 and self.__board[2][2] == 1:
            return False
        elif self.__board[0][0] == 2 and self.__board[1][1] == 2 and self.__board[2][2] == 2:
            return False
        elif self.__board[0][2] == 2 and self.__board[1][1] == 2 and self.__board[2][0] == 2:
            return False
        elif self.__board[0][0] == 2 and self.__board[1][0] == 2 and self.__board[2][0] == 2:
            return False
        elif self.__board[0][1] == 2 and self.__board[1][1] == 2 and self.__board[2][1] == 2:
            return False
        elif self.__board[0][2] == 2 and self.__board[1][2] == 2 and self.__board[2][2] == 2:
            return False
        elif self.__board[0][0] == 2 and self.__board[0][1] == 2 and self.__board[0][2] == 2:
            return False
        elif self.__board[1][0] == 2 and self.__board[1][1] == 2 and self.__board[1][2] == 2:
            return False
        elif self.__board[2][0] == 2 and self.__board[2][1] == 2 and self.__board[2][2] == 2:
            return False
        else:
            return True

    def set_col_row(self, x, y):
        self.__col = y
        self.__row = x

    def roundcount(self, a):
        for it in self.__pos:
            for q in it:
                if q:
                    a += 1
                else:
                    pass
        return a


def game(background):
    tic = TicTacToe(background)
    pygame.display.set_caption("Tic Tac Toe")
    while True:
        pygame.time.delay(10)
        win.fill((129, 129, 129))
        tic._draw_line()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                cursor_pos = event.pos
                tic.sel_turn()
                tic.set_col_row(math.floor(cursor_pos[1] / SQUARE_SIZE), math.floor(cursor_pos[0] / SQUARE_SIZE))
        tic.draw_shape()
        tic.draw_tic_tac()
        pygame.display.update()
        count = 0
        count = tic.roundcount(count)
        if not tic.check_win() or count == 9:
            tic.__init__(background)
            pygame.time.delay(1000)
        else:
            pass


win = pygame.display.set_mode((301, 301))
