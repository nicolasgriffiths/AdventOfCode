import collections

INPUT_FILE_PATH = "2021/1/input.txt"


def main():
    last_3, count = collections.deque([], maxlen=3), 0
    with open(INPUT_FILE_PATH, "r") as f:
        for i, num_str in enumerate(f.read().split()):
            num = int(num_str)
            if i > 2 and num > last_3[0]:
                count += 1
            last_3.append(num)

    print(f"Result: {count}")


if __name__ == "__main__":
    main()
