import numpy as np
import math

INPUT_FILE_PATH = "2021/7/input.txt"


def compute_fuel(positions: np.ndarray, loc: int):
    dist = np.abs(positions - loc)
    fuel = (dist * (dist + 1)) / 2.0
    return np.sum(fuel)


def main():
    with open(INPUT_FILE_PATH, "r") as f:
        positions = np.array([int(pos) for pos in f.read().split(",")])

    min_fuel = float("+inf")
    for loc in range(positions.min(), positions.max() + 1):
        new_fuel = compute_fuel(positions, loc)
        if new_fuel < min_fuel:
            # print(new_fuel, loc)
            min_fuel = new_fuel

    print(f"Result: {min_fuel}")


if __name__ == "__main__":
    main()
