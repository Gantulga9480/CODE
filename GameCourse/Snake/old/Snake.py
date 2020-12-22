import pygame
import numpy as np
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 177, 76)
BLUE = (255, 0, 255)


def start():
    d = random.randint(1, 2)
    x, y = 0, 0
    food_x = random.randint(1, board_count - 1) * vel + 21
    food_y = random.randint(1, board_count - 1) * vel + 21
    if d == 1:
        ldir = "↓"
        x = random.randint(1, board_count - 1) * vel + 21
        y = 3 * vel + 21
    elif d == 2:
        ldir = "→"
        X = 3 * vel + 21
        y = random.randint(1, board_count - 1) * vel + 21
    snake.clear()
    snake.append([x, y, ldir])
    return food_x, food_y


def game(screen):
    def draw_board():
        for i in range(board_count + 1):
            pygame.draw.line(screen, WHITE, (20 + i * vel, 20), (20 + i * vel, 520))
            pygame.draw.line(screen, WHITE, (20, 20 + i * vel), (520, 20 + i * vel))

    def draw_snake(block_s):
        if block_s[2] == "↑":
            pygame.draw.rect(screen, RED, (block_s[0], block_s[1], shape, shape))
            block_s[1] -= vel
        elif block_s[2] == "↓":
            pygame.draw.rect(screen, RED, (block_s[0], block_s[1], shape, shape))
            block_s[1] += vel
        elif block_s[2] == "←":
            pygame.draw.rect(screen, RED, (block_s[0], block_s[1], shape, shape))
            block_s[0] -= vel
        elif block_s[2] == "→":
            pygame.draw.rect(screen, RED, (block_s[0], block_s[1], shape, shape))
            block_s[0] += vel
        return block_s.copy()

    def draw_line(block_a):
        head = [block_a[0] + int(shape/2), block_a[1] + int(shape/2)].copy()
        food = [food_x + int(shape/2), food_y + int(shape/2)].copy()
        pygame.draw.line(screen, BLUE, head, food, 1)
        pygame.draw.line(screen, BLUE, head, [21, head[1]], 1)
        pygame.draw.line(screen, BLUE, head, [head[0], 21], 1)
        pygame.draw.line(screen, BLUE, head, [520, head[1]], 1)
        pygame.draw.line(screen, BLUE, head, [head[0], 520], 1)

    pygame.display.set_caption("SNAKE")
    food_x, food_y = start()
    tmp = ""
    ldir = ""
    is_pause = False
    while True:
        tmp = snake[0][2]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()
            # ["↑", "↓", "←", "→"]
            if keys[pygame.K_DOWN]:
                if tmp == "↑":
                    if len(snake) == 1:
                        snake[0][2] = "↓"
                else:
                    snake[0][2] = "↓"
            elif keys[pygame.K_UP]:
                if tmp == "↓":
                    if len(snake) == 1:
                        snake[0][2] = "↑"
                else:
                    snake[0][2] = "↑"
            elif keys[pygame.K_RIGHT]:
                if tmp == "←":
                    if len(snake) == 1:
                        snake[0][2] = "→"
                else:
                    snake[0][2] = "→"
            elif keys[pygame.K_LEFT]:
                if tmp == "→":
                    if len(snake) == 1:
                        snake[0][2] = "←"
                else:
                    snake[0][2] = "←"
            elif keys[pygame.K_SPACE]:
                if not is_pause:
                    is_pause = True
                    pause(screen)
                    pygame.display.set_caption("SNAKE")
                    is_pause = False
                else:
                    is_pause = False
        screen.fill((0, 0, 0))
        draw_board()
        for index, block in enumerate(snake):
            if index == 0:
                pass
            elif index > 0:
                tmp = block[2]
                block[2] = ldir
            if block[0] == food_x and block[1] == food_y:
                food_x = random.randint(1, board_count - 1) * vel + 21
                food_y = random.randint(1, board_count - 1) * vel + 21
                tail = snake[len(snake) - 1].copy()
                if tail[2] == "↑":
                    tail[1] += vel
                elif tail[2] == "↓":
                    tail[1] -= vel
                elif tail[2] == "←":
                    tail[0] += vel
                elif tail[2] == "→":
                    tail[0] -= vel
                snake.append(tail)
            else:
                pass
            pygame.draw.rect(screen, GREEN, (food_x, food_y, shape, shape))
            if block[1] < 20:
                # snake[index]= draw_snake([block[0], 521 - vel, ldir], board_count)
                food_x, food_y = start()
                main()
            elif block[1] > 520:
                # snake[index]= draw_snake([block[0], 21, ldir], board_count)
                food_x, food_y = start()
                main()
            elif block[0] < 20:
                # snake[index]= draw_snake([521 - vel, block[1], ldir], board_count)
                food_x, food_y = start()
                main()
            elif block[0] > 520:
                # snake[index]= draw_snake([21, block[1], ldir], board_count)
                food_x, food_y = start()
                main()
            else:
                snake[index] = draw_snake(block.copy())
            ldir = tmp
            if index == 0:
                draw_line(block.copy())
        # pygame.time.delay(vel * 2)
        pygame.display.update()
        clock.tick(40)


def pause(win):
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pause")
    run = True
    while run:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                run = False
        pygame.display.flip()
        clock.tick(60)


def main():
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Main")
    run = True
    while run:
        win.fill(RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                run = False
                game(win)
            else:
                pass
        pygame.display.flip()
        clock.tick(30)


width = 540
height = 600
vel = 25  # Changing velocity variable also changes number of rows, columns and game speed
shape = vel - 1
board_count = int((width - 40) / vel)
snake = list()
pygame.init()
clock = pygame.time.Clock()

if __name__ == "__main__":
    main()

pygame.quit()
quit()
