import pygame

pygame.init()

win = pygame.display.set_mode((255, 255))
pygame.display.set_caption("Color wheel")
clock = pygame.time.Clock()

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    x, y = pygame.mouse.get_pos()
    win.fill((x, y, 112))
    pygame.display.update()
    clock.tick(60)
