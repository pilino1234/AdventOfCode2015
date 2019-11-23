moves = {"(": 1, ")": -1}

def move(filename):
    floor = 0
    with open(filename) as file:
        for pos, i in enumerate(file.read()):
            floor += moves[i]
            if floor < 0:
                return pos + 1

print(move("day1-1-input.txt"))
