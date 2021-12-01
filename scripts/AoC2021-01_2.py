previous_sum = float('inf')
increased = 0

with open('../inputs/AoC2021-01.txt', 'r') as f:
    queue = [int(f.readline()) for _ in range(3)]
    for line in f:
        queue.append(int(line))
        if queue.pop(0) < queue[-1]:
            increased += 1

print(increased)
