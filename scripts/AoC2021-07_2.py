with open('../inputs/AoC2021-07.txt', 'r') as f:
    positions = [int(p) for p in f.read().split(',')]

print(min([sum([abs(pos - p) * (abs(pos - p) + 1) // 2 for p in positions]) for pos in range(max(positions))]))
