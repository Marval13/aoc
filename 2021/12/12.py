from __future__ import annotations
from typing import List, Union
from copy import deepcopy


class Path:
    def __init__(self, base: List[str]) -> None:
        self.p: List[str] = base
        self.twice: Union[str, None] = None

    def append(self, v: str) -> None:
        self.p.append(v)

    def copy(self) -> Path:
        p = Path(self.p.copy())
        p.twice = self.twice
        return p

    def contains(self, v: str) -> bool:
        return v in self.p

    def last(self) -> str:
        return self.p[-1]


class Graph:
    def __init__(self, edges: List[List[str]]) -> None:
        self.g: dict[str, List[str]] = {}
        for e in edges:
            self.g.setdefault(e[0], []).append(e[1])
            self.g.setdefault(e[1], []).append(e[0])

    # This sucks, will probably rewrite
    def paths(self, two: bool = False) -> List[List[str]]:
        flag = True
        paths = [Path(["start"])]

        while(flag):
            flag = False
            new_paths: List[Path] = []
            for p in paths:
                if p.last() == "end":
                    new_paths.append(p)
                    continue

                for v in self.g[p.last()]:
                    if v != "start":
                        if v.isupper() or not p.contains(v):
                            new_paths.append(p.copy())
                            new_paths[-1].append(v)
                            flag = True
                        elif two and p.twice is None:
                            new_paths.append(p.copy())
                            new_paths[-1].append(v)
                            new_paths[-1].twice = v
                            flag = True

            paths = deepcopy(new_paths)

        return [p.p for p in paths]


if __name__ == "__main__":
    with open("input.txt") as file:
        data: List[List[int]] = []
        for l in list(file):
            data.append(l.strip().split("-"))

    g = Graph(data)

    # Part One
    print(len(g.paths()))

    # Part Two
    print(len(g.paths(two=True)))
