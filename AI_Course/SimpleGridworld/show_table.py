import pygame
import numpy as np


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 177, 76)
BLUE = (255, 0, 255)
YELLOW = (255, 255, 0)

WIDTH = 361
HEIGHT = 361
VEL = 60
SHAPE = 59


def draw_game():
    for i in range(7):
        pygame.draw.line(win, BLACK, (i*VEL, 0), (i*VEL, 360))
        pygame.draw.line(win, BLACK, (0, i*VEL), (360, i*VEL))
    for i in range(6):
        for j in range(6):
            # 0 = up
            # 1 = down
            # 2 = left
            # 3 = right

            score = q_table[i][j]
            string1 = f"{round(score[0], 5)} up"
            string2 = f"{round(score[1], 5)} down"
            string3 = f"{round(score[2], 5)} left"
            string4 = f"{round(score[3], 5)} right"
            s = font.render(string1, 1, BLACK)
            win.blit(s, (j*VEL+5, i*VEL))
            s = font.render(string2, 1, BLACK)
            win.blit(s, (j*VEL+5, i*VEL+10))
            s = font.render(string3, 1, BLACK)
            win.blit(s, (j*VEL+5, i*VEL+20))
            s = font.render(string4, 1, BLACK)
            win.blit(s, (j*VEL+5, i*VEL+30))


pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 10)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Q_Table")
q_table = np.load("q_table.npy")
run = True
load_every = 50
# i = 0
while run:
    win.fill(WHITE)
    draw_game()
    try:
        q_table = np.load("q_table.npy", allow_pickle=True)
    except IOError as error:
        pass
    except ValueError:
        pass
    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
