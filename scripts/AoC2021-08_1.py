count = 0
with open('../inputs/AoC2021-08.txt', 'r') as f:
    for line in f:
        for digit in line.split('|')[1].strip().split(' '):
            if len(digit) in {2, 3, 4, 7}:
                count += 1

print(count)

