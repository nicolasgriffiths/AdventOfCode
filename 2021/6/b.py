from dataclasses import dataclass
from typing import Tuple

INPUT_FILE_PATH = "2021/6/input.txt"


def step(state):
    return {
        0: state[1],
        1: state[2],
        2: state[3],
        3: state[4],
        4: state[5],
        5: state[6],
        6: state[7] + state[0],
        7: state[8],
        8: state[0],
    }


def main():
    state = {num: 0 for num in range(9)}
    with open(INPUT_FILE_PATH, "r") as f:
        for num in f.read().split(","):
            state[int(num)] += 1
    print(state)

    for i in range(256):
        state = step(state)

    print(f"Result: {sum(state.values())}")


if __name__ == "__main__":
    main()
