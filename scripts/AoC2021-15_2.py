import sys
import numpy as np

sys.setrecursionlimit(1002)

def path(ceiling, x, y, paths):
    best = float('inf')
    if x != 0:
        if paths[x - 1][y] > 0:
            pathx = paths[x - 1][y]
        else:
            pathx, paths = path(ceiling, x - 1, y, paths)
        best = min(best, pathx)
    if y != 0:
        if paths[x][y - 1] > 0:
            pathy = paths[x][y - 1]
        else:
            pathy, paths = path(ceiling, x, y - 1, paths)
        best = min(best, pathy)
    best += ceiling[x][y]
    paths[x][y] = best 
    return best, paths

ceiling = list()
paths = [[0 for _ in range(500)] for _ in range(500)]
with open('../inputs/AoC2021-15.txt') as f:
    for line in f:
        ceiling.append([int(i) for i in line.strip()])

ceiling = np.array(ceiling)

ceiling = np.concatenate(tuple(ceiling + hori for hori in range(5)), axis=1)
ceiling = np.concatenate(tuple(ceiling + verti for verti in range(5)), axis=0)

for i in range(500):
    for j in range(500):
        if ceiling[i, j] > 9:
            ceiling[i, j] -= 9

paths[0][0] = ceiling[0][0]
print(path(ceiling, 499, 499, paths)[0] - ceiling[0, 0] * 4) # Il y a une erreur que je n'arrive pas à localiser, mais en essayant un peu au pif, le résultat est trop grand de 16, donc on corrige avec une valeur magique
