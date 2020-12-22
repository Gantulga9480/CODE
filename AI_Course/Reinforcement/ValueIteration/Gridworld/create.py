import numpy as np
import Gridworld.game as game


class Create(game.GridWorld):

    def __init__(self, envi=None, table=None, size=None):
        super().__init__(envi=envi, table=table, size=size)
        self.font = game.pygame.font.SysFont("arial", 40)
        self.choice = game.HOLE
        self.is_agent_placed = False
        self.is_treasure_placed = False
        self.hole_count = 0
        self.env = np.zeros((size, size))

    def create_env(self):
        game.pygame.display.set_caption("Make Env")
        while self.run:
            for event in game.pygame.event.get():
                if event.type == game.pygame.QUIT:
                    self.run = False
                if event.type == game.pygame.MOUSEBUTTONDOWN:
                    cursor_pos = event.pos
                    x = int(np.floor(cursor_pos[0] / self.vel))
                    y = int(np.floor(cursor_pos[1] / self.vel))
                    if self.choice == game.AGENT and not self.is_agent_placed:
                        if self.env[y][x] > 0:
                            pass
                        else:
                            self.env[y][x] = game.AGENT
                            self.is_agent_placed = True
                    elif self.choice == game.HOLE:
                        if self.env[y][x] > 0:
                            pass
                        else:
                            self.env[y][x] = game.HOLE
                            self.hole_count += 1
                    elif self.choice == game.TARGET:
                        if self.env[y][x] > 0:
                            pass
                        else:
                            self.env[y][x] = game.TARGET
                            self.is_treasure_placed = True
                if event.type == game.pygame.KEYDOWN:
                    if event.key == game.pygame.K_a:
                        if not self.is_agent_placed:
                            self.choice = game.AGENT
                    elif event.key == game.pygame.K_f:
                        self.choice = game.HOLE
                    elif event.key == game.pygame.K_d:
                        if not self.is_treasure_placed:
                            self.choice = game.TARGET
                    elif event.key == game.pygame.K_r:
                        self.env = np.zeros((self.size, self.size))
                        self.hole_count = 0
                        self.is_agent_placed = False
                        self.is_treasure_placed = False
                    elif event.key == game.pygame.K_q:
                        poss = game.pygame.mouse.get_pos()
                        x = int(np.floor(poss[0] / self.vel))
                        y = int(np.floor(poss[1] / self.vel))
                        if self.env[y][x] == game.HOLE:
                            self.env[y][x] = 0
                            self.hole_count -= 1
                        elif self.env[y][x] == game.AGENT:
                            self.env[y][x] = 0
                            self.is_agent_placed = False
                        elif self.env[y][x] == game.TARGET:
                            self.env[y][x] = 0
                            self.is_treasure_placed = False
                    elif event.key == game.pygame.K_s:
                        if self.is_agent_placed and self.is_treasure_placed \
                                and self.hole_count >= 0:
                            np.save("env", self.env)
                            np.save("v_table", self.q_table)
                            self.run = False
                        else:
                            pass
            self.draw_border()
            self.draw_board()
            if not self.run:
                game.pygame.image.save(self.win, game.ENV)
            count = self.font.render(f"{self.hole_count}", 1, game.BLUE)
            self.win.blit(count, (0, 0))
            game.pygame.display.flip()
            self.clock.tick(self.fps)
        game.pygame.display.quit()
