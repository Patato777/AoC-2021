op_to_cl = {'(': ')', '[': ']', '{': '}', '<': '>'}
score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
score = 0

with open('../inputs/AoC2021-10.txt', 'r') as f:
    for line in f:
        stack = list()
        for char in line.strip():
            if char in op_to_cl.keys():
                stack.append(op_to_cl[char])
            elif char != stack.pop():
                score += score_table[char]
                break

print(score)

