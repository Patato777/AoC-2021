op_to_cl = {'(': ')', '[': ']', '{': '}', '<': '>'}
score_table = {')': 1, ']': 2, '}': 3, '>': 4}
scores = list()

with open('../inputs/AoC2021-10.txt', 'r') as f:
    for line in f:
        stack = list()
        corrupted = False
        score = 0
        for char in line.strip():
            if char in op_to_cl.keys():
                stack.append(op_to_cl[char])
            elif char != stack.pop():
                score += score_table[char]
                corrupted = True
                break
        if not corrupted:
            for c in reversed(stack):
                score = 5 * score + score_table[c]
            scores.append(score)


print(sorted(scores)[len(scores) // 2])

