from typing import List
from copy import deepcopy


class HeightMap:
    def __init__(self, grid: List[List[int]]) -> None:
        l = len(grid[0])
        if not all(map(lambda x: len(x) == l, grid)):
            raise Exception("wrong data")

        self.xmax = l
        self.ymax = len(grid)
        self.grid = deepcopy(grid)
        self.basinchart = [[-1] * l for _ in range(0, len(grid))]

    def __repr__(self) -> str:
        return "\n".join(["".join([str(n) for n in row]) for row in self.grid])

    def print_basins(self) -> None:
        print("\n".join(["".join([str(n) for n in row])
                        for row in self.basinchart]))

    def is_low_point(self, x: int, y: int) -> bool:
        # Lint ignores because flake8 can't decide whether I should break
        # before of after a binary operator, this mutes the warnings.
        # Also the ignore makes the lines too long, so I muted that too.
        return (
            (x == 0 or self.grid[y][x] < self.grid[y][x - 1]) and               # noqa: W504, E501
            (x == self.xmax - 1 or self.grid[y][x] < self.grid[y][x + 1]) and   # noqa: W504, E501
            (y == 0 or self.grid[y][x] < self.grid[y - 1][x]) and               # noqa: W504, E501
            (y == self.ymax - 1 or self.grid[y][x] < self.grid[y + 1][x])
        )

    def risk_level(self, x: int, y: int) -> int:
        if not self.is_low_point(x, y):
            return 0
        return self.grid[y][x] + 1

    def neighbours(self, x: int, y: int) -> List[List[int]]:
        n: List[List[int]] = []
        if x > 0:
            n.append([x - 1, y])
        if y > 0:
            n.append([x, y - 1])
        if x < self.xmax - 1:
            n.append([x + 1, y])
        if y < self.ymax - 1:
            n.append([x, y + 1])
        return n

    def explore(self, x: int, y: int) -> int:
        if self.basinchart[y][x] > -1:
            return 0
        if self.grid[y][x] == 9:
            self.basinchart[y][x] = 0
            return 0
        self.basinchart[y][x] = 1
        count = 1
        for b in self.neighbours(x, y):
            count += self.explore(b[0], b[1])

        return count


if __name__ == "__main__":
    with open("input.txt") as file:
        data: List[List[int]] = []
        for l in list(file):
            data.append([int(n) for n in l.strip()])

        hm = HeightMap(data)

    # Part One
    count = 0
    for y in range(0, hm.ymax):
        for x in range(0, hm.xmax):
            count += hm.risk_level(x, y)

    print(count)

    # Part Two
    basins: List[int] = []
    for y in range(0, hm.ymax):
        for x in range(0, hm.xmax):
            b = hm.explore(x, y)
            if b > 0:
                basins.append(b)

    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])
