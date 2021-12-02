INPUT_FILE_PATH = "2021/2/input.txt"


def main():
    horizontal, depth = 0, 0
    with open(INPUT_FILE_PATH, "r") as f:
        for command in f.read().split("\n"):
            direction, num = command.split()
            if direction == "up":
                depth -= int(num)
            elif direction == "down":
                depth += int(num)
            elif direction == "forward":
                horizontal += int(num)
            else:
                print(f"Problems! {command}")
    print(f"Result: {horizontal * depth}")


if __name__ == "__main__":
    main()
