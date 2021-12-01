previous_sum = float('inf')
increased = 0

with open('../inputs/AoC2021-01.txt', 'r') as f:
    d1, d2 = int(f.readline()), int(f.readline())
    previous = [d1 + d2, d2]
    for line in f:
        previous.append(0)
        for i in range(3):
            previous[i] += int(line)
        new_sum = previous.pop(0)
        if new_sum > previous_sum:
            increased += 1
        previous_sum = new_sum

print(increased)
