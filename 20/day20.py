from collections import defaultdict
from typing import Dict


def distribute_presents(n: int) -> Dict[int, int]:
    houses = defaultdict(int)

    for i in range(1, n // 10):
        for j in range(i, n // 10, i):
            houses[j] += i * 10

    return houses


def distribute_presents_again(n: int) -> Dict[int, int]:
    houses = defaultdict(int)

    for elf_number in range(1, n // 10):
        counter = 0
        for house_number in range(elf_number, n // 10, elf_number):
            houses[house_number] += elf_number * 11
            counter += 1
            if counter == 50:
                break

    return houses


if __name__ == '__main__':
    with open("input.txt") as file:
        presents = int(file.readline())

    house_presents = distribute_presents(presents)

    for house in sorted(house_presents.keys()):
        if house_presents[house] >= presents:
            print(f"Part 1: {house}")
            break

    house_presents = distribute_presents_again(presents)

    for house in sorted(house_presents.keys()):
        if house_presents[house] >= presents:
            print(f"Part 2: {house}")
            break
