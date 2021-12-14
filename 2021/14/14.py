from typing import Dict, List


def pairify(s: str) -> Dict[str, int]:
    d: Dict[str, int] = {}
    for i in range(0, len(s) - 1):
        d.setdefault(s[i:i + 2], 0)
        d[s[i:i + 2]] += 1

    return d


def step(base: Dict[str, int], rules: Dict[str, str]) -> Dict[str, int]:
    new: Dict[str, int] = {}
    for key in base:
        new.setdefault(key[0] + rules[key], 0)
        new[key[0] + rules[key]] += base[key]

        new.setdefault(rules[key] + key[1], 0)
        new[rules[key] + key[1]] += base[key]

    return new


def count(polymer: Dict[str, int], more: List[str]) -> int:
    count: Dict[str, int] = {}
    for key in polymer:
        count.setdefault(key[0], 0)
        count[key[0]] += polymer[key]
        count.setdefault(key[1], 0)
        count[key[1]] += polymer[key]

    for key in count:
        count[key] = count[key] // 2

    for c in more:
        count.setdefault(c, 0)
        count[c] += 1

    most = max(count, key=count.get)
    least = min(count, key=count.get)

    return count[most] - count[least]


if __name__ == "__main__":
    with open("input.txt") as file:
        base: str
        rules: Dict[str, str] = {}
        for l in list(file):
            if l == "\n":
                continue
            elif "-" in l:
                a, b = l.strip().split(" -> ")
                rules[a] = b
            else:
                base = l.strip()

    d = pairify(base)

    # Part One
    for i in range(0, 10):
        d = step(d, rules)

    print(count(d, [base[0], base[-1]]))

    # Part Two
    for i in range(0, 30):
        d = step(d, rules)

    print(count(d, [base[0], base[-1]]))
