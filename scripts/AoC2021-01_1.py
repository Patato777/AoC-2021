previous = float('inf')
increased = 0

with open('../inputs/AoC2021-01.txt', 'r') as f:
    for line in f:
        if int(line) > previous:
            increased += 1
        previous = int(line)

print(increased)
