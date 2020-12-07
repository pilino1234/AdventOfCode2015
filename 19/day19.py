import re
from collections import defaultdict
from typing import List, Dict, Set


def parse(line_data: List[str]) -> Dict[str, List[str]]:
    parsed_reps = defaultdict(list)
    for line in line_data:
        if not line:
            break
        from_, _, to = line.partition(' => ')
        parsed_reps[from_].append(to)

    return parsed_reps


def calibrate(molecule: str, subs: Dict[str, List[str]]) -> Set[str]:
    created = set()
    for src, dests in subs.items():
        start = 0
        while True:
            pos = molecule.find(src, start)
            if pos == -1:
                break

            for dest in dests:
                created.add(molecule[:pos] + dest + molecule[pos + len(src):])

            start = pos + len(src)
    
    return created


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.strip() for line in file]

    replacements = parse(lines)
    print(replacements)

    calibration_molecule = lines[-1]
    print(calibration_molecule)

    calibration = calibrate(calibration_molecule, replacements)

    print(f"Part 1: {len(calibration)}")

    # Part 2, based on https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju/
    # Reverse the molecule string
    mol = calibration_molecule[::-1]

    # Create a literal reverse lookup table: reverse the table, and reverse all strings in the table too
    reverse_reps = {}
    for src, dests in replacements.items():
        for dest in dests:
            reverse_reps[dest[::-1]] = src[::-1]

    count = 0
    while mol != 'e':
        # Create an OR match of all the reversed replacement destinations
        # Use the returned match object to 'undo' the replacement in the molecule
        mol = re.sub('|'.join(reverse_reps.keys()), lambda m: reverse_reps[m.group()], mol, 1)
        # print(mol[::-1])
        count += 1

    print(f"Part 2: {count}")
