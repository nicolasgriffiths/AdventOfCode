INPUT_FILE_PATH = "2021/1/input.txt"


def main():
    last, count = None, 0
    with open(INPUT_FILE_PATH, "r") as f:
        for i, num_str in enumerate(f.read().split()):
            num = int(num_str)
            if i != 0 and num > last:
                count += 1
            last = num
    print(f"Result: {count}")


if __name__ == "__main__":
    main()
