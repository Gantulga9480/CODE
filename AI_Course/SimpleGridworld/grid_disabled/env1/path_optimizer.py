import numpy as np


q_table = np.load("q_table.npy")

LEN = len(q_table)


def get_path(q_table):
    path = np.zeros((LEN, LEN), dtype='<U11')
    for i in range(LEN):
        for j in range(LEN):
            action = np.argmax(q_table[i][j])
            if action == 0:
                path[i][j] = "↑"
            elif action == 1:
                path[i][j] = "↓"
            elif action == 2:
                path[i][j] = "→"
            elif action == 3:
                path[i][j] = "←"
    return path


print(get_path(q_table))
