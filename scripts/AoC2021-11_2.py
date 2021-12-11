def flash(cave):
    count = 0
    flashing = set()
    for x in range(1, 11):
        for y in range(1, 11):
            cave[x][y] += 1
            if cave[x][y] > 9:
                flashing.add((x, y))
    while flashing != set():
        for x in range(1, 11):
            print(cave[x][1:11])
        print('')
        #print(flashing)
        new_flashing = set()
        for octopus in flashing:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i != 0 or j != 0) and cave[octopus[0] + i][octopus[1] + j] >= 0 and cave[octopus[0]][octopus[1]] >= 0:
                        cave[octopus[0] + i][octopus[1] + j] += 1
                        #print(f'{(octopus[0], octopus[1]), (octopus[0] + i, octopus[1] + j), cave[octopus[0] + i][octopus[1] + j]}')
                        if cave[octopus[0] + i][octopus[1] + j] > 9:
                            new_flashing.add((octopus[0] + i, octopus[1] + j))
            cave[octopus[0]][octopus[1]] = -1
        flashing = new_flashing
    for x in range(1, 11):
        for y in range(1, 11):
            if cave[x][y] == -1:
                cave[x][y] = 0
                count += 1
        print(cave[x][1:11])
    return cave, count

                        

cave = [[-1 for _ in range(12)]]
with open('../inputs/AoC2021-11.txt', 'r') as f:
    for line in f:
        cave.append([-1] + [int(i) for i in line.strip()] + [-1])

cave.append([-1 for _ in range(12)])

flashes = 0
step = 0
while flashes < 100:
    cave, flashes = flash(cave)
    step += 1
    print('---')

print(step)
