from typing import List, Dict, Set, Tuple


def parse_analysis(lines: List[str]) -> Dict[str, int]:
    parsed = {}
    for line in lines:
        k, v = line.split(': ')
        parsed[k] = int(v)
    return parsed


def parse_sue(lines: List[str]) -> List[Dict[str, int]]:
    parsed = []
    for line in lines:
        _, _, compounds = line.partition(': ')
        parsed.append(parse_analysis(compounds.split(', ')))

    return parsed


def validate_sue(sue, expected) -> bool:
    for key in sue:
        if key in expected:
            if sue[key] != expected[key]:
                return False
    return True


def validate_sue_again(sue, expected) -> bool:
    for key in sue:
        if key in expected:
            if key in ('cats', 'trees'):
                if not (sue[key] > expected[key]):
                    return False
            elif key in ('pomeranians', 'goldfish'):
                if not (sue[key] < expected[key]):
                    return False
            else:
                if sue[key] != expected[key]:
                    return False
    return True


def find_matching(sue_list: List[Dict[str, int]], expected: Dict[str, int],
                  retroencabulator: bool = False) -> int:
    for idx, sue in enumerate(sue_list):
        if retroencabulator:
            if validate_sue_again(sue, expected):
                return idx + 1
        else:
            if validate_sue(sue, expected):
                return idx + 1


if __name__ == '__main__':
    with open("mfcsam.txt") as file:
        analysis_lines = [line.strip() for line in file]

    scan = parse_analysis(analysis_lines)

    with open("input.txt") as file:
        sue_lines = [line.strip() for line in file]

    sues = parse_sue(sue_lines)

    print(f"Part 1: {find_matching(sues, scan)}")
    print(f"Part 2: {find_matching(sues, scan, retroencabulator=True)}")

