import numpy as np

TAIL = 11
HEAD = 22


class Brain:

    def __init__(self, vel, board_count, shape):
        self.vel = vel
        self.board_count = board_count
        self.shape = shape

    def check_row(self, row, head_index, tail):
        tail_y = int((tail[0] - 21) / self.vel)
        tail_x = int((tail[1] - 21) / self.vel)
        diraction = ""
        side = [False, False]
        for ind, item in enumerate(row):
            if item == TAIL:
                if ind < head_index:
                    side[0] = True
                else:
                    side[1] = True
            else:
                pass
        if side[0]:
            if side[1]:
                if head_index + 1 == self.board_count or row[head_index + 1] == TAIL:
                    diraction = "←"
                elif row[head_index - 1] == TAIL:
                    diraction = "→"
                else:
                    if tail_y > head_index:
                        diraction = "→"
                    else:
                        diraction = "←"
            else:
                diraction = "→"
        elif side[1]:
            if side[0]:
                if row[head_index + 1] == TAIL:
                    diraction = "←"
                elif row[head_index - 1] == TAIL:
                    diraction = "→"
                else:
                    if tail_y > head_index:
                        diraction = "→"
                    else:
                        diraction = "←"
            else:
                diraction = "←"
        else:
            diraction = "→"
        return diraction

    def check_column(self, column, head_index, tail):
        tail_y = int((tail[0] - 21) / self.vel)
        tail_x = int((tail[1] - 21) / self.vel)
        diraction = ""
        side = [False, False]
        for ind, item in enumerate(column):
            if item == TAIL:
                if ind < head_index:
                    side[0] = True
                else:
                    side[1] = True
            else:
                pass
        if side[0]:
            if side[1]:
                if head_index + 1 == self.board_count or column[head_index + 1] == TAIL:
                    diraction = "↑"
                elif column[head_index - 1] == TAIL:
                    diraction = "↓"
                else:
                    if tail_y > head_index:
                        diraction = "↓"
                    else:
                        diraction = "↑"
            else:
                diraction = "↓"
        elif side[1]:
            if side[0]:
                if column[head_index + 1] == TAIL:
                    diraction = "↑"
                elif column[head_index - 1] == TAIL:
                    diraction = "↓"
                else:
                    if tail_y > head_index:
                        diraction = "↓"
                    else:
                        diraction = "↑"
            else:
                diraction = "↑"
        else:
            diraction = "↓"
        return diraction

    def move(self, head, tail, board, food):
        hi_x = int((head[0] - 21)/self.vel)
        hi_y = int((head[1] - 21)/self.vel)
        head_x = head[0]
        head_y = head[1]
        food_x = food[0]
        food_y = food[1]
        head_dir = head[2]
        next_move = head[2]
        x = food_x - head_x
        y = food_y - head_y
        if x < 0 and y < 0:
            if head_dir == "↓":
                if hi_x == 0 or board[hi_y][hi_x-1] == TAIL:
                    if hi_y == self.board_count - 1 or board[hi_y+1][hi_x] == TAIL:
                        next_move = "→"
                    else:
                        pass
                else:
                    next_move = "←"
            elif head_dir == "→":
                if hi_y == 0 or board[hi_y-1][hi_x] == TAIL:
                    if hi_x == self.board_count - 1 or board[hi_y][hi_x+1] == TAIL:
                        next_move = "↓"
                    else:
                        pass
                else:
                    next_move = "↑"
            else:
                if head_dir == "←":
                    if board[hi_y][hi_x-1] == TAIL:
                        col = np.transpose(board)
                        next_move = self.check_column(col[hi_x], hi_y, tail)
                elif head_dir == "↑":
                    if board[hi_y-1][hi_x] == TAIL:
                        next_move = self.check_row(board[hi_y], hi_x, tail)
        elif x < 0 and y > 0:
            if head_dir == "↑":
                if hi_x == 0 or board[hi_y][hi_x-1] == TAIL:
                    if hi_y == 0 or board[hi_y-1][hi_x] == TAIL:
                        pass
                    else:
                        next_move = "→"
                else:
                    next_move = "←"
            elif head_dir == "→":
                if hi_y == self.board_count - 1 or board[hi_y+1][hi_x] == TAIL:
                    if hi_x == self.board_count - 1 or board[hi_y][hi_x+1] == TAIL:
                        next_move = "↑"
                    else:
                        pass
                else:
                    next_move = "↓"
            else:
                if head_dir == "←":
                    if board[hi_y][hi_x-1] == TAIL:
                        col = np.transpose(board)
                        next_move = self.check_column(col[hi_x], hi_y, tail)
                elif head_dir == "↓":
                    if board[hi_y+1][hi_x] == TAIL:
                        next_move = self.check_row(board[hi_y], hi_x, tail)
        elif x > 0 and y > 0:
            if head_dir == "↑":
                if hi_x == self.board_count - 1 or board[hi_y][hi_x+1] == TAIL:
                    if hi_y == 0 or board[hi_y-1][hi_x] == TAIL:
                        next_move = "←"
                    else:
                        pass
                else:
                    next_move = "→"
            elif head_dir == "←":
                if hi_y == self.board_count - 1 or board[hi_y+1][hi_x] == TAIL:
                    if hi_x == 0 or board[hi_y][hi_x-1] == TAIL:
                        next_move = "↑"
                    else:
                        pass
                else:
                    next_move = "↓"
            else:
                if head_dir == "→":
                    if board[hi_y][hi_x+1] == TAIL:
                        col = np.transpose(board)
                        next_move = self.check_column(col[hi_x], hi_y, tail)
                elif head_dir == "↓":
                    if board[hi_y+1][hi_x] == TAIL:
                        next_move = self.check_row(board[hi_y], hi_x, tail)
        elif x > 0 and y < 0:
            if head_dir == "↓":
                if hi_x == self.board_count - 1 or board[hi_y][hi_x+1] == TAIL:
                    if hi_y == self.board_count - 1 or board[hi_y+1][hi_x] == TAIL:
                        next_move = "←"
                    else:
                        pass
                else:
                    next_move = "→"
            elif head_dir == "←":
                if hi_y == 0 or board[hi_y-1][hi_x] == TAIL:
                    if hi_x == 0 or board[hi_y][hi_x-1] == TAIL:
                        next_move = "↓"
                    else:
                        pass
                else:
                    next_move = "↑"
            else:
                if head_dir == "→":
                    if board[hi_y][hi_x+1] == TAIL:
                        col = np.transpose(board)
                        next_move = self.check_column(col[hi_x], hi_y, tail)
                elif head_dir == "↑":
                    if board[hi_y-1][hi_x] == TAIL:
                        next_move = self.check_row(board[hi_y], hi_x, tail)
        elif x == 0 and y > 0:
            if head_dir == "↑":
                if hi_x == 0 or board[hi_y][hi_x - 1] == TAIL:
                    if hi_x == self.board_count - 1 or board[hi_y][hi_x + 1] == TAIL:
                        pass
                    else:
                        next_move = "→"
                elif hi_x == self.board_count - 1 or board[hi_y][hi_x + 1] == TAIL:
                    next_move = "←"
                else:
                    next_move = self.check_row(board[hi_y], hi_x, tail)
            else:
                if head_dir == "↓":
                    if board[hi_y+1][hi_x] == TAIL:
                        next_move = self.check_row(board[hi_y], hi_x, tail)
                    else:
                        next_move = "↓"
                elif head_dir == "←":
                    if hi_y == self.board_count - 1 or board[hi_y+1][hi_x] == TAIL:
                        if hi_x == 0 or board[hi_y][hi_x-1] == TAIL:
                            next_move = "↑"
                        else:
                            pass
                    else:
                        next_move = "↓"
                elif head_dir == "→":
                    if hi_y == self.board_count - 1 or board[hi_y+1][hi_x] == TAIL:
                        if hi_x == self.board_count - 1 or board[hi_y][hi_x+1] == TAIL:
                            next_move = "↑"
                        else:
                            pass
                    else:
                        next_move = "↓"
        elif x == 0 and y < 0:
            if head_dir == "↓":
                if hi_x == 0 or board[hi_y][hi_x - 1] == TAIL:
                    if hi_x == self.board_count - 1 or board[hi_y][hi_x + 1] == TAIL:
                        pass
                    else:
                        next_move = "→"
                elif hi_x == self.board_count - 1 or board[hi_y][hi_x + 1] == TAIL:
                    next_move = "←"
                else:
                    next_move = self.check_row(board[hi_y], hi_x, tail)
            else:
                if head_dir == "↑":
                    if board[hi_y-1][hi_x] == TAIL:
                        next_move = self.check_row(board[hi_y], hi_x, tail)
                    else:
                        next_move = "↑"
                elif head_dir == "←":
                    if hi_y == 0 or board[hi_y-1][hi_x] == TAIL:
                        if hi_x == 0 or board[hi_y][hi_x-1] == TAIL:
                            next_move = "↓"
                        else:
                            pass
                    else:
                        next_move = "↑"
                elif head_dir == "→":
                    if hi_y == 0 or board[hi_y-1][hi_x] == TAIL:
                        if hi_x == self.board_count - 1 or board[hi_y][hi_x+1] == TAIL:
                            next_move = "↓"
                        else:
                            pass
                    else:
                        next_move = "↑"
        elif x > 0 and y == 0:
            if head_dir == "←":
                if hi_y == 0 or board[hi_y - 1][hi_x] == TAIL:
                    if hi_y == self.board_count - 1 or board[hi_y + 1][hi_x] == TAIL:
                        pass
                    else:
                        next_move = "↓"
                elif hi_y == self.board_count - 1 or board[hi_y + 1][hi_x] == TAIL:
                    next_move = "↑"
                else:
                    col = np.transpose(board)
                    next_move = self.check_column(col[hi_x], hi_y, tail)
            else:
                if head_dir == "→":
                    if board[hi_y][hi_x+1] == TAIL:
                        col = np.transpose(board)
                        next_move = self.check_column(col[hi_x], hi_y, tail)
                    else:
                        next_move = "→"
                elif head_dir == "↑":
                    if hi_x == self.board_count - 1 or board[hi_y][hi_x+1] == TAIL:
                        if hi_y == 0 or board[hi_y-1][hi_x] == TAIL:
                            next_move = "←"
                        else:
                            pass
                    else:
                        next_move = "→"
                elif head_dir == "↓":
                    if hi_x == self.board_count - 1 or board[hi_y][hi_x+1] == TAIL:
                        if hi_y == self.board_count - 1 or board[hi_y+1][hi_x] == TAIL:
                            next_move = "←"
                        else:
                            pass
                    else:
                        next_move = "→"

        elif x < 0 and y == 0:
            if head_dir == "→":
                if hi_y == 0 or board[hi_y - 1][hi_x] == TAIL:
                    if hi_y == self.board_count - 1 or board[hi_y + 1][hi_x] == TAIL:
                        pass
                    else:
                        next_move = "↓"
                elif hi_y == self.board_count - 1 or board[hi_y + 1][hi_x] == TAIL:
                    next_move = "↑"
                else:
                    col = np.transpose(board)
                    next_move = self.check_column(col[hi_x], hi_y, tail)
            else:
                if head_dir == "←":
                    if board[hi_y][hi_x-1] == TAIL:
                        col = np.transpose(board)
                        next_move = self.check_column(col[hi_x], hi_y, tail)
                    else:
                        next_move = "←"
                elif head_dir == "↑":
                    if hi_x == 0 or board[hi_y][hi_x-1] == TAIL:
                        if hi_y == self.board_count - 1 or board[hi_y+1][hi_x] == TAIL:
                            pass
                        else:
                            next_move = "→"
                    else:
                        next_move = "←"
                elif head_dir == "↓":
                    if hi_x == 0 or board[hi_y][hi_x-1] == TAIL:
                        if hi_y == self.board_count - 1 or board[hi_y+1][hi_x] == TAIL:
                            next_move = "→"
                        else:
                            pass
                    else:
                        next_move = "←"

        elif x == 0 and y == 0:
            if head_dir == "→":
                if hi_x == self.board_count - 1 or board[hi_y][hi_x+1] == TAIL:
                    if board[hi_y-1][hi_x] != TAIL:
                        next_move = "↑"
                    else:
                        next_move = "↓"
                else:
                    pass
            elif head_dir == "↑":
                if hi_y == 0 or board[hi_y-1][hi_x] == TAIL:
                    if board[hi_y][hi_x-1] != TAIL:
                        next_move = "←"
                    else:
                        next_move = "→"
                else:
                    pass
            elif head_dir == "↓":
                if hi_y == self.board_count - 1 or board[hi_y+1][hi_x] == TAIL:
                    if board[hi_y][hi_x-1] != TAIL:
                        next_move = "←"
                    else:
                        next_move = "→"
                else:
                    pass
            elif head_dir == "←":
                if hi_x == 0 or board[hi_y][hi_x-1] == TAIL:
                    if board[hi_y-1][hi_x] != TAIL:
                        next_move = "↑"
                    else:
                        next_move = "↓"
                else:
                    pass
        return next_move
