from typing import List


class Board():
    def __init__(self, numbers: List[int]):
        self.marked = [[False] * 5 for _ in range(0, 5)]
        self.numbers = numbers.copy()
        self.last = -1

    def __repr__(self) -> str:
        return "\n".join(
            [" ".join([str(n).rjust(2) for n in row]) for row in self.numbers]
        )

    def check(self) -> bool:
        for row in self.marked:
            if all(row):
                return True

        for col in range(0, 5):
            if all([row[col] for row in self.marked]):
                return True

        return False

    def mark(self, n: int) -> bool:
        self.last = n
        for i in range(0, 5):
            for j in range(0, 5):
                if self.numbers[i][j] == n:
                    self.marked[i][j] = True
                    return True

        return False

    def score(self) -> int:
        score = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if not self.marked[i][j]:
                    score += self.numbers[i][j]
        return score * self.last


def lottery(boards: List[Board], draws: List[int]) -> Board:
    for n in draws:
        for board in boards:
            board.mark(n)
            if board.check():
                return board


def antilottery(boards: List[Board], draws: List[int]) -> Board:
    for i, n in enumerate(draws):
        for board in boards:
            board.mark(n)
        boards = [b for b in boards if not b.check()]
        if len(boards) == 1:
            return lottery(boards, draws[i + 1:])


if __name__ == "__main__":
    with open("input.txt") as file:
        draws: List[int] = []
        boards: List[Board] = []
        part = []
        for i, l in enumerate(list(file)):
            if i == 0:
                draws = [int(n) for n in l.split(",")]
            elif i == 1 or l == "\n":
                pass
            else:
                part.append([int(n) for n in l.split()])
                if len(part) == 5:
                    boards.append(Board(part))
                    part = []

    # Part One
    winner = lottery(boards, draws)

    print("Winner:")
    print(winner)
    print(winner.score())

    # Part Two
    loser = antilottery(boards, draws)

    print("Loser:")
    print(loser)
    print(loser.score())
