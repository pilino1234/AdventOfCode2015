import re
from collections import defaultdict
from itertools import permutations
from typing import List, Dict, Tuple


def parse_combinations(input_lines: List[str], include_self = False) -> Dict[str, Dict[str, int]]:
    happiness_dict: Dict[str, Dict[str, int]] = defaultdict(dict)

    regex = re.compile(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).")

    for line in input_lines:
        data = regex.match(line)
        person1, gain_lose, amount, person2 = data.groups()

        happiness_dict[person1][person2] = int(amount) * (1 if 'gain' in gain_lose else -1)

        if include_self:
            happiness_dict[person1]['self'] = 0
            happiness_dict['self'][person1] = 0

    return happiness_dict


def happiness_for_seating(seating: Tuple[str], happiness_dict: Dict[str, Dict[str, int]]) -> int:
    total_happiness = 0
    for idx, person in enumerate(seating):
        right_neighbour = seating[(idx + 1) % len(seating)]
        left_neighbour = seating[(idx - 1) % len(seating)]
        total_happiness += happiness_dict[person][right_neighbour] + happiness_dict[person][left_neighbour]

    return total_happiness


def find_maximum_happiness(happiness_dict: Dict[str, Dict[str, int]]):
    best_happiness = None
    for p in permutations(happiness_dict.keys()):
        total_happiness = happiness_for_seating(p, happiness_dict)

        if best_happiness is None:
            best_happiness = total_happiness
            continue
        if total_happiness > best_happiness:
            best_happiness = total_happiness

    return best_happiness


if __name__ == '__main__':
    with open("test.txt") as file:
        lines = [line.strip() for line in file]

    happiness = parse_combinations(lines)
    assert find_maximum_happiness(happiness) == 330

    with open("input.txt") as file:
        lines = [line.strip() for line in file]

    happiness = parse_combinations(lines)
    print(find_maximum_happiness(happiness))

    happiness = parse_combinations(lines, include_self = True)
    print(find_maximum_happiness(happiness))
