pos = [0, 0]

with open('../inputs/AoC2021-02.txt', 'r') as file:
    for line in file:
        direction, steps = line.split(' ')
        if direction == 'forward':
            pos[0] += int(steps)
        elif direction == 'down':
            pos[1] += int(steps)
        else:
            pos[1] -= int(steps)

print(pos[0] * pos[1])
