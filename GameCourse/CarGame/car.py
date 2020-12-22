import pygame

pygame.init()
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
CAR_WIDTH = 74
CAR_HEIGHT = 92
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
VELOCITY = 2

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Pygame Tut")
clock = pygame.time.Clock()

carImg = pygame.image.load("res\img\car.png")

def car(x, y):
    gameDisplay.blit(carImg, (x, y))
    pygame.draw.lines(gameDisplay, GREEN, True,
                        [(x, y), (x + CAR_WIDTH, y),
                         (x + CAR_WIDTH, y + CAR_HEIGHT),
                         (x, y + CAR_HEIGHT)])

def move(keys, x, y):
    temp_x = x
    temp_y = y
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        temp_y -= VELOCITY - 0.6
        temp_x += VELOCITY - 0.6
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        temp_y -= VELOCITY - 0.6
        temp_x -= VELOCITY - 0.6
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        temp_y += VELOCITY - 0.6
        temp_x -= VELOCITY - 0.6
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        temp_y += VELOCITY - 0.6
        temp_x += VELOCITY - 0.6
    elif keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        pass
    elif keys[pygame.K_UP] and keys[pygame.K_DOWN]:
        pass
    elif keys[pygame.K_UP]:
        temp_y -= VELOCITY
    elif keys[pygame.K_DOWN]:
        temp_y += VELOCITY
    elif keys[pygame.K_LEFT]:
        temp_x -= VELOCITY
    elif keys[pygame.K_RIGHT]:
        temp_x += VELOCITY
    if temp_x > DISPLAY_WIDTH - CAR_WIDTH or temp_x < 0:
        if temp_y > DISPLAY_HEIGHT - CAR_HEIGHT or temp_y < 0:
            return x, y
        else:
            return x, temp_y
    elif temp_y > DISPLAY_HEIGHT - CAR_HEIGHT or temp_y < 0:
        if temp_x > DISPLAY_WIDTH - CAR_WIDTH or temp_x < 0:
            return x, y
        else:
            return temp_x, y
    else:
        return temp_x, temp_y

x = float(DISPLAY_WIDTH * 0.5)
y = float(DISPLAY_HEIGHT * 0.8)

game = True

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    x, y = move(keys, x, y)
    
    if x > DISPLAY_WIDTH - CAR_WIDTH or x < 0:
        crashed = True
    else:
        gameDisplay.fill(WHITE)
        car(round(x), round(y))
        pygame.display.update()
        clock.tick(60)

pygame.quit()
quit()
