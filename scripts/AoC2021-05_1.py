vents = [set(), set()]
with open('../inputs/AoC2021-05.txt', 'r') as f:
    for line in f:
        ends = [eval(e) for e in line.split(' -> ')]
        if ends[0][0] == ends[1][0] or ends[0][1] == ends[1][1]:
            for i in range(min(ends[0][0], ends[1][0]), max(ends[0][0], ends[1][0]) + 1):
                for j in range(min(ends[0][1], ends[1][1]), max(ends[0][1], ends[1][1]) + 1):
                    if (i, j) in vents[0]:
                        vents[0].remove((i, j))
                        vents[1].add((i, j))
                    elif (i, j) not in vents[1]:
                        vents[0].add((i, j))

print(len(vents[1]))

