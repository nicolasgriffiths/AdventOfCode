INPUT_FILE_PATH = "2021/2/input.txt"


def main():
    horizontal, depth, aim = 0, 0, 0
    with open(INPUT_FILE_PATH, "r") as f:
        for command in f.read().split("\n"):
            direction, num = command.split()
            num = int(num)
            if direction == "up":
                aim -= num
            elif direction == "down":
                aim += num
            elif direction == "forward":
                horizontal += num
                depth += aim * num
            else:
                print(f"Problems! {command}")
    print(f"Result: {horizontal}, {depth}, {aim}")
    print(f"Result: {horizontal * depth}")


if __name__ == "__main__":
    main()
