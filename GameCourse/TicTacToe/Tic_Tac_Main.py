import sys
import pygame
import alpha
import tic_class as tic

def options(font1, background1):

    op = True
    opt = pygame.display.set_mode((301, 500))
    pygame.display.set_caption("Options")
    font_1 = pygame.font.SysFont(alpha.Fonts.font1, 25)
    font_2 = pygame.font.SysFont(alpha.Fonts.font2, 25)

    while op:
        opt.fill(background1)
        my_font1 = pygame.font.SysFont(font1, 25)
        label = my_font1.render("Font    Color", 1, alpha.Colors.BLACK)
        opt.blit(label, (80, 15))
        pygame.draw.rect(opt, alpha.Colors.BLACK, (50, 50, 140, 50))
        label = font_1.render("Font 1", 1, alpha.Colors.WHITE)
        opt.blit(label, (80, 65))
        pygame.draw.rect(opt, alpha.Colors.GREEN, (200, 50, 50, 50))
        pygame.draw.rect(opt, alpha.Colors.BLACK, (50, 115, 140, 50))
        label = font_2.render("Font 2", 1, alpha.Colors.WHITE)
        opt.blit(label, (80, 130))
        pygame.draw.rect(opt, alpha.Colors.WHITE, (200, 115, 50, 50))
        pygame.draw.rect(opt, alpha.Colors.BLACK, (50, 180, 200, 50))
        label1 = my_font1.render("Back", 1, alpha.Colors.WHITE)
        opt.blit(label1, (120, 195))

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            if events.type == pygame.MOUSEBUTTONUP:
                cursor_pos1 = events.pos
                if 50 <= cursor_pos1[0] <= 190 and 50 <= cursor_pos1[1] <= 100:
                    font1 = alpha.Fonts.font1
                if 50 <= cursor_pos1[0] <= 190 and 115 <= cursor_pos1[1] <= 165:
                    font1 = alpha.Fonts.font2
                if 50 <= cursor_pos1[0] <= 250 and 180 <= cursor_pos1[1] <= 230:
                    op = False
                if 200 <= cursor_pos1[0] <= 250 and 50 <= cursor_pos1[1] <= 100:
                    background1 = alpha.Colors.GREEN
                if 200 <= cursor_pos1[0] <= 250 and 115 <= cursor_pos1[1] <= 165:
                    background1 = alpha.Colors.WHITE
        pygame.display.update()
        pygame.time.delay(100)
    return font1, background1


def main():
    font = alpha.Fonts.font1
    background = alpha.Colors.WHITE
    desk = pygame.display.set_mode((301, 301))
    pygame.display.set_caption("Tic Tac Toe")

    while True:
        desk.fill(background)
        my_font = pygame.font.SysFont(font, 25)
        title = pygame.font.SysFont(font, 40)
        end = pygame.font.SysFont(font, 20)
        label = title.render("TIC TAC TOE", 1, alpha.Colors.BLACK)
        desk.blit(label, (30, 5))
        pygame.draw.rect(desk, alpha.Colors.BLACK, (50, 50, 200, 50))
        label = my_font.render("Start game", 1, alpha.Colors.WHITE)
        desk.blit(label, (80, 65))
        pygame.draw.rect(desk, alpha.Colors.BLACK, (50, 115, 200, 50))
        label = my_font.render("Options", 1, alpha.Colors.WHITE)
        desk.blit(label, (100, 130))
        pygame.draw.rect(desk, alpha.Colors.BLACK, (50, 180, 200, 50))
        label = my_font.render("Exit", 1, alpha.Colors.WHITE)
        desk.blit(label, (120, 195))
        label = end.render("B181070038 Г. Гантулга", 1, alpha.Colors.BLACK)
        desk.blit(label, (30, 240))
        label = end.render("© 2020 OOP HOME WORK ", 1, alpha.Colors.BLACK)
        desk.blit(label, (30, 270))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                cursor_pos = event.pos
                if 50 <= cursor_pos[0] <= 250 and 50 <= cursor_pos[1] <= 100:
                    tic.game(background)
                if 50 <= cursor_pos[0] <= 250 and 115 <= cursor_pos[1] <= 165:
                    font, background = options(font, background)
                if 50 <= cursor_pos[0] <= 250 and 180 <= cursor_pos[1] <= 230:
                    sys.exit()
        pygame.display.update()
        pygame.time.delay(100)


pygame.init()
main()
