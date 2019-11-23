
def literal_length(string: str) -> int:
    return len(string)


def memory_length(string: str) -> int:
    return len(eval(string))


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    part1 = sum(literal_length(line) for line in lines) - sum(memory_length(line) for line in lines)
    print(part1)

    encoded_length = sum(2 + line.count('\\') + line.count('"') for line in lines)
    print(encoded_length)
