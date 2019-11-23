moves = {"(": 1, ")": -1}

def move(filename):
    with open(filename) as file:
        return sum(moves[i] for i in file.read())

print(move("day1-1-input.txt"))
