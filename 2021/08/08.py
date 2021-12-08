from typing import Dict, List


if __name__ == "__main__":
    with open("input.txt") as file:
        data: List[Dict[str, List[str]]] = []
        for l in list(file):
            s, o = l.split("|")
            data.append({
                "signals": list(map("".join, map(sorted, s.split()))),
                "output": list(map("".join, map(sorted, o.split()))),
            })

    # Part One
    count = 0
    for display in data:
        for o in display["output"]:
            if len(o) <= 4 or len(o) == 7:
                count += 1

    print(count)

    # Part Two
    def inters(s1: str, s2: str) -> int:
        count = 0
        for c in s1:
            if c in s2:
                count += 1
        return count

    displays: List[int] = []

    for display in data:
        digits: List[str] = [""] * 10

        # I should really install Python 3.10
        for s in display["signals"]:
            if len(s) == 2:
                digits[1] = s
            elif len(s) == 3:
                digits[7] = s
            elif len(s) == 4:
                digits[4] = s
            elif len(s) == 7:
                digits[8] = s

        for s in display["signals"]:
            if len(s) == 5:
                if inters(s, digits[4]) == 2:
                    digits[2] = s
                elif inters(s, digits[1]) == 2:
                    digits[3] = s
                else:
                    digits[5] = s
            elif len(s) == 6:
                if inters(s, digits[1]) == 1:
                    digits[6] = s
                elif inters(s, digits[4]) == 3:
                    digits[0] = s
                else:
                    digits[9] = s

        displays.append(int("".join([
            str(digits.index(o)) for o in display["output"]
        ])))

    # print(displays)
    print(sum(displays))
