class Board():
    def __init__(self):
        self.content = list()
        self.marked = set()

    def add_line(self, line):
        to_list = [int(line[i:i + 2].strip()) for i in range(0, 14, 3)]
        self.content.extend(to_list)

    def mark(self, nb):
        if nb in self.content:
            ind = self.content.index(nb)
            self.content[ind] = 0
            self.marked.add(divmod(ind, 5))

    def check_win(self):
        for i in range(5):
            if {(i, j) for j in range(5)}.issubset(self.marked) or {(j, i) for j in range(5)}.issubset(self.marked):
                return True
        return False
    
    def score(self):
        return sum(self.content)


boards = list()

with open('../inputs/AoC2021-04.txt', 'r') as f:
    draw = f.readline().strip().split(',')
    for line in f:
        if line == '\n':
            boards.append(Board())
        else:
            boards[-1].add_line(line)


def drawing(draw, boards):
    for nb in draw:
        nb = int(nb)
        new_boards = list()
        for board in boards:
            board.mark(nb)
            if board.check_win():
                if len(boards) == 1:
                    return nb * board.score()
            else:
                new_boards.append(board)
        boards = new_boards


print(drawing(draw, boards))

