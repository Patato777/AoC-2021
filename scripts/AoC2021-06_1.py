with open('../inputs/AoC2021-06.txt', 'r') as f:
    fishes = [int(i) for i in f.read().split(',')]

for _ in range(80):
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1

print(len(fishes))
