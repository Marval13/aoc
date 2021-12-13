from typing import List, Literal, Tuple, Union
from copy import deepcopy
import itertools


class Sheet:
    def __init__(self, dots: List[List[int]]) -> None:
        self.xmax = max([d[0] for d in dots]) + 1
        self.ymax = max([d[1] for d in dots]) + 1
        self.dots = deepcopy(dots)
        self.dots.sort()

    def __repr__(self) -> str:
        s = []
        for y in range(0, self.ymax):
            line = ""
            for x in range(0, self.xmax):
                if [x, y] in self.dots:
                    line += "#"
                else:
                    line += "."
            s.append(line)
        return "\n".join(s)

    def fold(
        self,
        direction: Union[Literal["x"], Literal["y"]],
        axis: int
    ) -> int:
        count = 0
        if direction == "x":
            self.xmax = axis
            for i, d in enumerate(self.dots):
                if d[0] > axis:
                    diff = d[0] - axis
                    newd = [(d[0] - 2 * diff), d[1]]
                    if newd in self.dots:
                        count += 1
                    self.dots[i] = newd
        else:
            self.ymax = axis
            for i, d in enumerate(self.dots):
                if d[1] > axis:
                    diff = d[1] - axis
                    newd = [d[0], (d[1] - 2 * diff)]
                    if newd in self.dots:
                        count += 1
                    self.dots[i] = newd
        self.dots.sort()
        self.dots = [l for l, _ in itertools.groupby(self.dots)]
        return count

    def visible_dots(self) -> int:
        return len(self.dots)


if __name__ == "__main__":
    with open("input.txt") as file:
        data: List[List[int]] = []
        folds: List[Tuple[str, int]] = []
        for l in list(file):
            if l == "\n":
                continue
            if l[0] == "f":
                t = l.strip().split()[2].split("=")
                folds.append((t[0], int(t[1])))
            else:
                data.append(list(map(int, l.strip().split(","))))

    sheet = Sheet(data)

    # Part One
    # print(sheet.visible_dots())
    # print(sheet.fold(*folds[0]))
    # print(sheet.visible_dots())

    # Part Two
    for f in folds:
        sheet.fold(*f)

    print(sheet)
