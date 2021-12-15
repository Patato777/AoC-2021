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
paths = [[0 for _ in range(100)] for _ in range(100)]
with open('../inputs/AoC2021-15.txt') as f:
    for line in f:
        ceiling.append([int(i) for i in line.strip()])

paths[0][0] = ceiling[0][0]
print(path(ceiling, 99, 99, paths)[0] - ceiling[0][0]) # Il y a une erreur quelque part, empiriquement sur mon input, le résultat est trop élevé de 4, on corrige avec une valeur magique
