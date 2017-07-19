

def is_nice(string):
    if has_pair_things(string):
        if has_repeat_letter_thing(string):
            return True
    return False


def has_pair_things(string):
    return any([(string.count(string[i:i+2]) >= 2) for i in range(len(string) - 2)])


def has_repeat_letter_thing(string):
    return any([string[i] == string[i + 2] for i in range(len(string) - 2)])


if __name__ == "__main__":
    print(is_nice("ugknbfddgicrmopn"))
    print(is_nice("aaa"))
    print(is_nice("jchzalrnumimnmhp"))
    print(is_nice("haegwjzuvuyypxyu"))
    print(is_nice("dvszwmarrgswjxmb"))

    with open("Day5-input.txt") as file:
        lines = file.read().splitlines()
        print(sum(map(is_nice, lines)))
