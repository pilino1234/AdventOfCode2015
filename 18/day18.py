from typing import List

import numpy


class LightGrid:
    _nb8 = {(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)}

    def __init__(self, width, height, locked):
        self.width = width
        self.height = height
        self.grid = numpy.zeros((width, height), int)
        self.locked = locked

        if self.locked:
            self.grid[0, 0] = 1
            self.grid[-1, 0] = 1
            self.grid[0, -1] = 1
            self.grid[-1, -1] = 1

    def __str__(self):
        return str(self.grid)

    def switch(self, x: int, y: int, on: bool):
        self.grid[y, x] = int(on)

    @classmethod
    def neighbours(cls, x, y):
        for pt in cls._nb8:
            yield x + pt[0], y + pt[1]

    def existing_neighbours(self, x, y):
        return [pt for pt in self.neighbours(x, y) if 0 <= pt[0] < self.width and 0 <= pt[1] < self.height]

    def simulate(self):
        next_grid = self.grid.copy()
        for idy, row in enumerate(self.grid):
            for idx, col in enumerate(row):
                if self.locked and (idx, idy) in [(0, 0), (self.width-1, 0), (0, self.height-1),
                                                  (self.width-1, self.height-1)]:
                    continue

                neighbouring = [self.grid[nb[1], nb[0]] for nb in self.existing_neighbours(idx, idy)]
                on_nbs = sum(neighbouring)
                current = self.grid[idy, idx]
                if current:
                    if not 2 <= on_nbs <= 3:
                        next_grid[idy, idx] = 1 - current
                else:
                    if on_nbs == 3:
                        next_grid[idy, idx] = 1 - current

        self.grid = next_grid

    @property
    def active_lights(self) -> int:
        return self.grid.sum()


def parse(line_data: List[str], locked: bool = False) -> LightGrid:
    height = len(line_data)
    width = len(line_data[0])
    new_grid = LightGrid(width, height, locked)
    for y, line in enumerate(line_data):
        for x, char in enumerate(line):
            if char == '#':
                new_grid.switch(x, y, True)
    return new_grid


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.strip() for line in file]

    grid = parse(lines)

    for _ in range(100):
        grid.simulate()

    print(f"Part 1: {grid.active_lights}")

    grid2 = parse(lines, locked=True)
    for _ in range(100):
        grid2.simulate()

    print(f"Part 2: {grid2.active_lights}")
