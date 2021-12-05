from __future__ import annotations
from typing import List


# Points are also vectors
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Point) -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def normalize(self) -> Point:
        x = 0
        if self.x > 0:
            x = 1
        elif self.x < 0:
            x = -1

        y = 0
        if self.y > 0:
            y = 1
        elif self.y < 0:
            y = -1

        return Point(x, y)


def line(p0: Point, p1: Point) -> List[Point]:
    dir = (p1 - p0).normalize()
    # Part One: ignore diagonal lines
    # if dir.x != 0 and dir.y != 0:
    #    return []

    l = [p0]
    p = p0
    while p != p1:
        p += dir
        l.append(p)

    return l


if __name__ == "__main__":
    with open("input.txt") as file:
        data: List[List[Point]] = []
        for l in list(file):
            p0, p1 = l.split(" -> ")
            data.append([
                Point(*[int(n) for n in p0.split(",")]),
                Point(*[int(n) for n in p1.split(",")])
            ])

    # I know this is bad but it works and also I don't care
    seen_points: set[Point] = set(())
    bad_points: set[Point] = set(())

    for p0, p1 in data:
        for p in line(p0, p1):
            if p in seen_points:
                bad_points.add(p)
            else:
                seen_points.add(p)

    print(len(bad_points))
