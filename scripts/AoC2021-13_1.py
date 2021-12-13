from numpy import array, count_nonzero, zeros, fliplr, flipud

def fold(table, axis, value):
    for i in range(value):
        if axis == 'x':
            return table[:value, :] + flipud(table[value + 1:, :])
        else:
            return table[:, :value] + fliplr(table[:, value + 1:])
    if axis == 'x':
        table = table[:value, :]
    else:
        table = table[:, :value]
    return table


def print_dotted(dotted):
    for row in dotted.T:
        for val in row:
            print('█', end='') if val else print(' ', end='')
        print('')


dotted = zeros((1311, 895), dtype='bool')
shape = [0, 0]
with open('../inputs/AoC2021-13.txt', 'r') as f:
    line = f.readline()
    while line != '\n':
        x, y = eval(line.strip())
        dotted[x, y] = True
        line = f.readline()
    line = f.readline()
    axis, value = line[11:].strip().split('=')
    dotted = fold(dotted, axis, int(value))

print(count_nonzero(dotted))
    

