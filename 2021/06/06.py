from typing import List


def cycle(data: List[int]):
    resets = fish.pop(0)
    fish.append(resets)
    fish[6] += resets


if __name__ == "__main__":
    with open("input.txt") as file:
        data = [int(n) for n in file.read().strip().split(",")]
        fish = [0] * 9
        for i in range(0, 8):
            fish[i] = data.count(i)

    # Part One
    # days = 80

    # Part Two
    days = 256

    for _ in range(0, days):
        cycle(fish)

    print(sum(fish))
