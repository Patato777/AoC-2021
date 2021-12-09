def greatest_slope(i, j):
    lowest = min([(i, j), (i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)], key=lambda t: hmap[t[0]][t[1]][0])
    if lowest == (i, j):
        hmap[i][j][1] = 100 * i + j
        basins[100 * i + j] = basins[100 * i + j] + 1 if 100 * i + j in basins.keys() else 1
        return 100 * i + j
    elif hmap[lowest[0]][lowest[1]][1] >= 0:
        hmap[i][j][1] = hmap[lowest[0]][lowest[1]][1]
        basins[hmap[lowest[0]][lowest[1]][1]] += 1
        return hmap[lowest[0]][lowest[1]][1]
    else:
        hmap[i][j][1] = greatest_slope(*lowest)
        basins[hmap[i][j][1]] += 1
        return hmap[i][j][1]

basins = dict()
hmap = [[[10, -1] for _ in range(102)]]
with open('../inputs/AoC2021-09.txt', 'r') as f:
    for line in f:
        line = line.strip()
        hmap.append([[10, -1]] + [[int(i), - 1] for i in line] + [[10, -1]])

hmap.append([[10, -1] for _ in range(102)])

for i in range(1, 101):
    for j in range(1, 101):
        if hmap[i][j][0] < 9 and hmap[i][j][1] <= 0:
            greatest_slope(i, j)

largest = sorted(basins.values())[-3:]
print(largest[0] * largest[1] * largest[2])
