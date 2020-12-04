from typing import List


def fill(volume: int, conts: List[int]) -> List[List[int]]:
    if not conts:
        return []
    if volume == 0:
        return []

    combos = []
    remaining_containers = conts.copy()
    for container in conts:
        remaining_containers.remove(container)

        if container > volume:
            continue
        if container == volume:
            combos.append([container])
            continue

        for combo in fill(volume - container, remaining_containers):
            combos.append([container] + combo)
    return combos


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.strip() for line in file]

    containers = list(map(int, lines))

    fills = fill(150, containers)

    print(f"Part 1: {len(fills)}")

    shortest_fill = min(map(len, fills))
    shortest_fill_count = sum(len(f) == shortest_fill for f in fills)
    print(f"Part 2: {shortest_fill_count}")

