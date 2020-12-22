import snake_game as sg
import snake_brain as sb

sg.init()
game = sg.Snake()

for episode in range(10000):
    state = game.reset()
    done = False
    while not done:
        done, next_state, r = game.step(auto=True)
