pos = [0, 0]
aim = 0

with open('../inputs/AoC2021-02.txt', 'r') as file:
    for line in file:
        direction, steps = line.split(' ')
        if direction == 'forward':
            pos[0] += int(steps)
            pos[1] += int(steps) * aim
        elif direction == 'down':
            aim += int(steps)
        else:
            aim -= int(steps)

print(pos[0] * pos[1])
