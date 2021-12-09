import numpy as np
import math

INPUT_FILE_PATH = "2021/7/input.txt"


def compute_fuel(positions: np.ndarray, loc: int):
    return np.sum(np.abs(positions - loc))


def main():
    with open(INPUT_FILE_PATH, "r") as f:
        positions = np.array([int(pos) for pos in f.read().split(",")])

    median = np.median(positions)
    median_down = math.floor(median)
    median_up = math.ceil(median)

    res = min(compute_fuel(positions, median_down), compute_fuel(positions, median_up))

    print(f"Result: {res}")


if __name__ == "__main__":
    main()
