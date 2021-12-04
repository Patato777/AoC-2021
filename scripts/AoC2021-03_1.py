table = [0] * 12

with open('../inputs/AoC2021-03.txt', 'r') as file:
    for line in file:
        line = line.strip()
        for i, letter in enumerate(line):
            if letter == '1':
                table[i] += 1
            else:
                table[i] -= 1

gamma = str()
epsilon = str()
for i in range(12):
    if table[i] > 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))
