from dataclasses import dataclass
from typing import Tuple

INPUT_FILE_PATH = "2021/5/input.txt"


@dataclass
class Line:
    start: Tuple[int, int]
    end: Tuple[int, int]

    @property
    def is_horizontal(self):
        return self.start[0] == self.end[0]

    @property
    def is_vertical(self):
        return self.start[1] == self.end[1]

    @property
    def is_diagonal(self):
        return abs(self.start[0] - self.end[0]) == abs(self.start[1] - self.end[1])


def plot_line(line: Line, grid):
    if line.is_horizontal:
        i = line.start[0]
        low = min(line.start[1], line.end[1])
        high = max(line.start[1], line.end[1])
        for j in range(low, high + 1):
            grid[i][j] += 1
    elif line.is_vertical:
        j = line.start[1]
        low = min(line.start[0], line.end[0])
        high = max(line.start[0], line.end[0])
        for i in range(low, high + 1):
            grid[i][j] += 1
    elif line.is_diagonal:
        incr_i = 1 if (line.end[0] - line.start[0]) > 0 else -1
        incr_j = 1 if (line.end[1] - line.start[1]) > 0 else -1
        for i, j in zip(
            range(line.start[0], line.end[0] + incr_i, incr_i),
            range(line.start[1], line.end[1] + incr_j, incr_j),
        ):
            grid[i][j] += 1
    else:
        raise Exception
    return grid


def main():
    # Parse lines
    lines = list()
    max_i = 0
    max_j = 0
    with open(INPUT_FILE_PATH, "r") as f:
        for l in f.readlines():
            substr_start, substr_end = l.split(" -> ")
            start_i, start_j = substr_start.split(",")
            end_i, end_j = substr_end.split(",")
            max_i = max(max_i, int(start_i), int(end_i))
            max_j = max(max_j, int(start_j), int(end_j))
            lines.append(
                Line(
                    start=(
                        int(start_i),
                        int(start_j),
                    ),
                    end=(
                        int(end_i),
                        int(end_j),
                    ),
                )
            )

    # Plot lines
    grid = [[0] * (max_j + 1) for _ in range(max_i + 1)]
    for l in lines:
        if l.is_horizontal or l.is_vertical or l.is_diagonal:
            grid = plot_line(l, grid)

    # Find where there are 2s or greater
    count = 0
    for row in grid:
        for cell in row:
            if cell >= 2:
                count += 1

    print(f"Result: {count}")


if __name__ == "__main__":
    main()
