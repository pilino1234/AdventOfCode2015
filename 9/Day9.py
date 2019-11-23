from typing import Tuple, List, Dict
from itertools import permutations


def parse_distances(lines: List[str]) -> Dict[Tuple[str, str], int]:
    distances = {}
    for line in lines:
        source, _, dest, _, distance = line.split()
        distances[(source, dest)] = int(distance)
        distances[(dest, source)] = int(distance)

    return distances


def find_shortest_and_longest(distance_tuples: Dict[Tuple[str, str], int]) -> Tuple[int, int]:
    places = set()
    for tup in distance_tuples:
        places.add(tup[0])
        places.add(tup[1])

    shortest = None
    longest = None
    for p in permutations(places):
        dist = sum(map(lambda x, y: distances[(x, y)], p[:-1], p[1:]))
        if shortest is None or longest is None:
            shortest = dist
            longest = dist
            continue
        if dist < shortest:
            shortest = dist
        if dist > longest:
            longest = dist

    return shortest, longest


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    distances = parse_distances(lines)

    (shortest, longest) = find_shortest_and_longest(distances)
    print(shortest)
    print(longest)

