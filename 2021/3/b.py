INPUT_FILE_PATH = "2021/3/input.txt"


def to_decimal(bin_iter):
    total = 0
    for i, num in enumerate(reversed(bin_iter)):
        if num == "1" or num == 1:
            total += 2 ** i
    return total


def count_zeros_and_ones_at(lines, pos):
    idx_zero, idx_one = [], []
    for i, line in enumerate(lines):
        if line[pos] == "1":
            idx_one.append(i)
        else:
            idx_zero.append(i)
    return idx_zero, idx_one


def filter_lines(lines, most_common):
    pos = 0
    while len(lines) > 1:
        idx_zero, idx_one = count_zeros_and_ones_at(lines, pos)
        zeros_common = len(idx_zero) > len(idx_one)
        condition = zeros_common if most_common else not zeros_common
        idx = idx_zero if condition else idx_one
        lines = [lines[i] for i in idx]
        pos += 1
    assert len(lines) == 1
    return lines[0].strip()


def main():
    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()

    # Get binary representations
    oxygen = filter_lines(lines, True)
    co2 = filter_lines(lines, False)

    # Convert to decimal
    oxygen = to_decimal(oxygen)
    co2 = to_decimal(co2)

    print(f"Result: {oxygen*co2}")


if __name__ == "__main__":
    main()
