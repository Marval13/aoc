from typing import List
from copy import deepcopy
from itertools import product


class Octopus:
    def __init__(self, energy: int) -> None:
        self.energy = energy

    def __repr__(self) -> str:
        return str(self.energy)

    def increase(self) -> None:
        self.energy += 1

    def flash(self) -> bool:
        if self.energy > 9:
            self.energy = 0
            return True
        return False

    def get_flashed(self) -> None:
        if self.energy > 0:
            self.increase()


class Grid:
    def __init__(self, grid: List[List[Octopus]]) -> None:
        self.grid = deepcopy(grid)

    def __repr__(self) -> str:
        return "\n".join(
            ["".join([str(o) + "|" for o in row]) for row in self.grid])

    def near(self, x: int, y: int) -> List[int]:
        return list(filter(
            lambda p: p[0] >= 0 and p[0] < 10 and           # noqa: W504
                      p[1] >= 0 and p[1] < 10 and           # noqa: W504, E131
                      (p[0] != x or p[1] != y),             # noqa: E131
            product([x - 1, x, x + 1], [y - 1, y, y + 1])
        ))

    def step(self) -> int:
        for row in self.grid:
            for o in row:
                o.increase()

        count = 0
        x, y = 0, 0
        while(x < 10 and y < 10):
            if self.grid[y][x].flash():
                count += 1
                list(map(
                    lambda p: self.grid[p[1]][p[0]].get_flashed(),
                    self.near(x, y)
                ))
                x = max(x - 1, 0)
                y = max(y - 1, 0)
            else:
                y += 1
                if y > 9:
                    x += 1
                    y = 0

        return count

    def sync(self) -> bool:
        return all([all([o.energy == 0 for o in row]) for row in self.grid])


if __name__ == "__main__":
    with open("input.txt") as file:
        data: List[List[int]] = []
        for l in list(file):
            data.append([int(n) for n in l.strip()])

    # Part One
    grid = Grid([[Octopus(n) for n in row] for row in data])

    flashes = 0
    for s in range(0, 100):
        flashes += grid.step()

    print(flashes)

    # Part Two
    grid = Grid([[Octopus(n) for n in row] for row in data])

    step = 0
    while not grid.sync():
        step += 1
        grid.step()

    print(step)
