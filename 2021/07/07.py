from statistics import median, mean
from math import floor

if __name__ == "__main__":
    with open("input.txt") as file:
        data = [int(n) for n in file.read().strip().split(",")]

    # Part One
    med = int(median(data))
    fuel1 = sum(map(lambda x: abs(x - med), data))

    print(med, fuel1)

    # Part Two

    # We need to minimize the sum of this function across the data.
    # By deriving it we obtain that the minimum between the mean
    # minus 1/2 and the mean plus 1/2.
    # Thus we just need to check the integers around these numbers to
    # be sure to get the right solution.

    m = floor(mean(data) - 0.5)
    cand = [m, m + 1, m + 2]

    def fuelfunc(i):
        return lambda x: int((abs(x - cand[i]) + 1) * abs(x - cand[i]) / 2)

    fuel2 = [
        sum(map(fuelfunc(0), data)),
        sum(map(fuelfunc(1), data)),
        sum(map(fuelfunc(2), data)),
    ]

    i = fuel2.index(min(fuel2))
    print(cand[i], fuel2[i])
