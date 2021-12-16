from typing import List, Tuple
from copy import deepcopy
from math import inf


class Graph:
    def __init__(self, nodes: List[List[int]], big: bool = False) -> None:
        if not big:
            self.nodes: List[List[int]] = deepcopy(nodes)

        else:
            def wrap(n: int) -> int:
                if n > 9:
                    n -= 9
                return n

            self.nodes: List[List[int]] = []

            for repy in range(0, 5):
                for row in nodes:
                    new_row = []
                    for repx in range(0, 5):
                        new_row += list(
                            map(lambda n: wrap(n + repx + repy), row))

                    self.nodes.append(new_row)

        self.ymax = len(self.nodes)
        self.xmax = len(self.nodes[0])

        self.distance = [[inf] * self.xmax for _ in range(0, self.ymax)]
        self.visited = [[False] * self.xmax for _ in range(0, self.ymax)]

        self.current = {(0, 0)}
        self.distance[0][0] = 0

        self.target = (self.xmax - 1, self.ymax - 1)

    def near(self, x: int, y: int) -> List[Tuple[int, int]]:
        n: List[List[int]] = []
        if x > 0:
            n.append((x - 1, y))
        if y > 0:
            n.append((x, y - 1))
        if x < self.xmax - 1:
            n.append((x + 1, y))
        if y < self.ymax - 1:
            n.append((x, y + 1))
        return n

    def set_distance(self, x: int, y: int) -> None:
        self.current.remove((x, y))
        self.visited[y][x] = True
        for v in self.near(x, y):
            if not self.visited[v[1]][v[0]]:
                self.distance[v[1]][v[0]] = min(
                    self.distance[y][x] + self.nodes[v[1]][v[0]],
                    self.distance[v[1]][v[0]]
                )
                self.current.add((v[0], v[1]))

    def step(self) -> None:
        n = min(self.current, key=lambda v: self.distance[v[1]][v[0]])
        self.set_distance(*n)

    def populate(self) -> int:
        while not self.visited[self.target[1]][self.target[0]]:
            n = min(self.current, key=lambda v: self.distance[v[1]][v[0]])
            self.set_distance(*n)

        return self.distance[self.target[1]][self.target[0]]


if __name__ == "__main__":
    with open("input.txt") as file:
        data: List[List[int]] = []
        for l in list(file):
            row = []
            for n in l.strip():
                row.append(int(n))
            data.append(row)

    g = Graph(data, big=True)
    print(g.populate())
