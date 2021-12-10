from typing import List, Tuple


def pair(o: str, c: str) -> bool:
    return ((o == "(" and c == ")") or  # noqa: W504
            (o == "[" and c == "]") or  # noqa: W504
            (o == "{" and c == "}") or  # noqa: W504
            (o == "<" and c == ">"))


def check(line: str) -> Tuple[str]:
    stack: List[str] = []
    for c in line:
        if c == "(" or c == "[" or c == "{" or c == "<":
            stack.append(c)
        else:
            c1 = stack.pop()
            if not pair(c1, c):
                return (c, stack)
    return ("", stack)


def score_corrupt(c: str, stack: List[str]) -> int:
    # Part One
    # The line is corrupted, so we only consider the character
    # returned as an error for the score
    if c == ")":
        return 3
    elif c == "]":
        return 57
    elif c == "}":
        return 1197
    elif c == ">":
        return 25137
    else:
        return 0


def score_complete(c: str, stack: List[str]) -> int:
    # Part Two
    # The line is incomplete: there were no errors so we only
    # consider the stack for the score
    if c != "":
        return 0

    s = 0
    while len(stack) > 0:
        a = stack.pop()
        if a == "(":
            t = 1
        elif a == "[":
            t = 2
        elif a == "{":
            t = 3
        elif a == "<":
            t = 4
        else:
            t = 0

        s *= 5
        s += t

    return s


if __name__ == "__main__":
    with open("input.txt") as file:
        data: List[str] = []
        for l in list(file):
            data.append(l.strip())

    # Part One
    total = sum([score_corrupt(*check(line)) for line in data])
    print(total)

    # Part Two
    scores = sorted(filter(
        lambda x: x > 0,
        [score_complete(*check(line)) for line in data]
    ))
    print(scores[(len(scores) - 1) // 2])
