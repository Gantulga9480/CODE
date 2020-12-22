import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 177, 76)
BLUE = (255, 0, 255)
YELLOW = (255, 255, 0)

VEL = 60
SHAPE = 59


def draw_board():
    for i in range(7):
        pygame.draw.line(win, WHITE, (i*VEL, 0), (i*VEL, 360))
        pygame.draw.line(win, WHITE, (0, i*VEL), (360, i*VEL))
    pygame.draw.rect(win, RED, (VEL*2+1, 1, SHAPE, SHAPE))
    pygame.draw.rect(win, RED, (VEL*3+1, 1, SHAPE, SHAPE))
    pygame.draw.rect(win, RED, (VEL*2+1, VEL*1+1, SHAPE, SHAPE))
    pygame.draw.rect(win, RED, (VEL*3+1, VEL*1+1, SHAPE, SHAPE))
    pygame.draw.rect(win, RED, (VEL*2+1, VEL*2+1, SHAPE, SHAPE))
    pygame.draw.rect(win, RED, (VEL*3+1, VEL*2+1, SHAPE, SHAPE))
    pygame.draw.rect(win, GREEN, (VEL*5+1, 1, SHAPE, SHAPE))
    pygame.draw.rect(win, YELLOW, (1, 1, SHAPE, SHAPE))


pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((361, 361))
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    win.fill(BLACK)
    # Boundary
    draw_board()

    pygame.display.flip()
    clock.tick(60)
