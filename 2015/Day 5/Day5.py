from itertools import groupby


def is_nice(string):
    if has_vowels(string, 3):
        if has_rep_letter(string, 2):
            if has_no_bad_string(string):
                return True
    return False


def has_vowels(string, number):
    return sum(map(string.count, "aeiou")) >= number


def has_rep_letter(string, number):
    for letter, group in groupby(string):
        if len(list(group)) >= number:
            return True
    return False


def has_no_bad_string(string):
    bad_list = ["ab", "cd", "pq", "xy"]
    return not any(bad_string in string for bad_string in bad_list)


if __name__ == "__main__":
    print(is_nice("ugknbfddgicrmopn"))
    print(is_nice("aaa"))
    print(is_nice("jchzalrnumimnmhp"))
    print(is_nice("haegwjzuvuyypxyu"))
    print(is_nice("dvszwmarrgswjxmb"))

    with open("Day5-input.txt") as file:
        lines = file.read().splitlines()
        print(sum(map(is_nice, lines)))
