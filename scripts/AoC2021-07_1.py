with open('../inputs/AoC2021-07.txt', 'r') as f:
    positions = [int(p) for p in f.read().split(',')]

print(min([sum([abs(pos - p) for p in positions]) for pos in range(max(positions))]))
