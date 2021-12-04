INPUT_FILE_PATH = "2021/3/input.txt"


def main():
    # Count 1s at each position
    counts_one = {}
    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        num_lines = len(lines)
        for line in lines:
            for i, char in enumerate(line.strip()):
                if char == "1":
                    counts_one[i] = counts_one.get(i, 0) + 1

    # Get binary number for gamma and epsilon
    half = num_lines / 2.0
    gamma = [0 if counts_one[k] < half else 1 for k in sorted(counts_one.keys())]
    epsilon = [0 if v == 1 else 1 for v in gamma]

    # Convert to decimal
    def to_decimal(bin_list):
        total = 0
        for i, num in enumerate(reversed(bin_list)):
            if num == 1:
                total += 2 ** i
        return total
    gamma = to_decimal(gamma)
    epsilon = to_decimal(epsilon)

    print(f"Result: {gamma*epsilon}")


if __name__ == "__main__":
    main()
