hmap = [[10 for _ in range(102)]]
with open('../inputs/AoC2021-09.txt', 'r') as f:
    for line in f:
        line = line.strip()
        hmap.append([10] + [int(i) for i in line] + [10])

hmap.append([10 for _ in range(102)])

print(sum([hmap[i][j] + 1 for i in range(1, 101) for j in range(1, 101) if hmap[i][j] < hmap[i - 1][j] and hmap[i][j] < hmap[i][j - 1] and hmap[i][j] < hmap[i + 1][j] and hmap[i][j] < hmap[i][j + 1]]))
            
