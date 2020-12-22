import numpy as np
import random

x = np.zeros((9, 9))
y = 0
# count = 0
row = False
col = False
box = False
check = True
for i in range(9):
    for j in range(9):
        while check:
            x[i][j] = random.randint(1, 9)
            for num in range(9):
                if x[i][j] == x[i][num]:
                    if num == j:
                        pass
                    else:
                        col = True
            for num2 in range(9):
                if x[i][j] == x[num2][j]:
                    if num2 == i:
                        pass
                    else:
                        row = True
            if i < 3 and j < 3:
                for a in range(3):
                    for a1 in range(3):
                        if x[i][j] == x[a][a1]:
                            if a == i and a1 == j:
                                pass
                            else:
                                box = True
                        else:
                            pass
            if i < 3 and 2 < j < 6:
                for a in range(3):
                    for a1 in range(3):
                        if x[i][j] == x[a][a1 + 3]:
                            if a == i and a1 + 3 == j:
                                pass
                            else:
                                box = True
                        else:
                            pass
            if i < 3 and 5 < j < 9:
                for a in range(3):
                    for a1 in range(3):
                        if x[i][j] == x[a][a1 + 6]:
                            if a == i and a1 + 6 == j:
                                pass
                            else:
                                box = True
                        else:
                            pass
            if 2 < i < 6 and j < 3:
                for a in range(3):
                    for a1 in range(3):
                        if x[i][j] == x[a + 3][a1]:
                            if a + 3 == i and a1 == j:
                                pass
                            else:
                                box = True
                        else:
                            pass
            if 2 < i < 6 and 2 < j < 6:
                for a in range(3):
                    for a1 in range(3):
                        if x[i][j] == x[a + 3][a1 + 3]:
                            if a + 3 == i and a1 + 3 == j:
                                pass
                            else:
                                box = True
                        else:
                            pass
            if 2 < i < 6 and 5 < j < 9:
                for a in range(3):
                    for a1 in range(3):
                        if x[i][j] == x[a + 3][a1 + 6]:
                            if a + 3 == i and a1 + 6 == j:
                                pass
                            else:
                                box = True
                        else:
                            pass
            if 5 < i < 9 and j < 3:
                for a in range(3):
                    for a1 in range(3):
                        if x[i][j] == x[a + 6][a1]:
                            if a + 6 == i and a1 == j:
                                pass
                            else:
                                box = True
                        else:
                            pass
            if 5 < i < 9 and 2 < j < 6:
                for a in range(3):
                    for a1 in range(3):
                        if x[i][j] == x[a + 6][a1 + 3]:
                            if a + 6 == i and a1 + 3 == j:
                                pass
                            else:
                                box = True
                        else:
                            pass
            if 5 < i < 9 and 5 < j < 9:
                for a in range(3):
                    for a1 in range(3):
                        if x[i][j] == x[a + 6][a1 + 6]:
                            if a + 6 == i and a1 + 6 == j:
                                pass
                            else:
                                box = True
                        else:
                            pass
            print(col, row, box, "\n", x)
            if row or col or box:
                row = False
                col = False
                box = False
            else:
                check = False
                row = False
                col = False
                box = False
        check = True

print(x)
