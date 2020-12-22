import snake_game as sg
import snake_brain as sb
import numpy as np

def get_action(self, state):
        next_state = [[state[0]-1, state[1]], [state[0]+1, state[1]],
                      [state[0], state[1]-1], [state[0], state[1]+1]]
        vals = list()
        for i, item in enumerate(next_state):
            try:
                if item[0] >= 0 and item[1] >= 0:
                    vals.append(self.v_table[item[0]][item[1]])
                else:
                    vals.append(self.hole_reward)
            except IndexError:
                vals.append(self.hole_reward)
        return np.argmax(vals)

sg.init()
game = sg.Snake()

for episode in range(10000):
    state = game.reset()
    done = False
    while not done:
        # action = np.argmax(model.predict(np.expand_dims(state, axis=0)))
        done, state, _ = game.step(auto=True)
