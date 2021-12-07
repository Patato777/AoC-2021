with open('../inputs/AoC2021-06.txt', 'r') as f:
    start = [int(i) for i in f.read().split(',')]

fishes = {0: len(start)}
for g0 in start:
    for gn in range(g0, 256, 7):
        if gn in fishes.keys():
            fishes[gn] += 1
        else:
            fishes[gn] = 1

for g in range(1, 256):
    if g in fishes.keys():
        for gn in range(g + 9, 256, 7):
            if gn in fishes.keys():
                fishes[gn] += fishes[g]
            else:
                fishes[gn] = fishes[g]

print(sum([v for v in fishes.values()]))
