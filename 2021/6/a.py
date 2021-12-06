from dataclasses import dataclass
from typing import Tuple

INPUT_FILE_PATH = "2021/6/input.txt"


def step(state):
    extra_fish = 0
    for i in range(len(state)):
        if state[i] != 0:
            state[i] = state[i] - 1
        else:
            state[i] = 6
            extra_fish += 1
    if extra_fish != 0:
        state = state + [8] * extra_fish
    return state


def main():
    with open(INPUT_FILE_PATH, "r") as f:
        state = [int(num) for num in f.read().split(",")]

    for i in range(80):
        state = step(state)

    print(f"Result: {len(state)}")


if __name__ == "__main__":
    main()
