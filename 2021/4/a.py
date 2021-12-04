INPUT_FILE_PATH = "2021/4/input.txt"


def get_board(lines, index_dict, board_num):
    board = []
    for i, line in enumerate(lines):
        if line == "\n":
            break
        row = []
        for j, num in enumerate(line.strip().split()):
            num_int = int(num)
            row.append(num_int)
            new_entry = [
                (
                    board_num,
                    i,
                    j,
                )
            ]
            index_dict[num_int] = index_dict.get(num_int, list()) + new_entry
        board.append(row)
    return board, index_dict, lines[i + 1 :]


def get_boards(lines):
    boards = []
    index_dict = {}
    while len(lines) > 1:
        board, index_dict, lines = get_board(lines, index_dict, len(boards))
        boards.append(board)
    return boards, index_dict


def mark_board_and_check(entry, boards):
    board_num, i, j = entry
    boards[board_num][i][j] = None
    if all([num is None for num in boards[board_num][i]]):
        return board_num
    if all(
        [boards[board_num][idx][j] is None for idx in range(len(boards[board_num]))]
    ):
        return board_num
    return None


def main():
    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        random_numbers = [int(num) for num in lines[0].strip().split(",")]
        boards, index_dict = get_boards(lines[2:])

    print(boards[14])
    for random_number in random_numbers:
        entries = index_dict.get(random_number, list())
        for entry in entries:
            board_num = mark_board_and_check(entry, boards)
            if board_num is not None:
                break
        if board_num is not None:
            break

    s = 0
    for row in boards[board_num]:
        for num in row:
            if num is not None:
                s += num

    print(f"Board {board_num} is the winner, with the last number {random_number}")
    print(f"Board set up: {boards[board_num]}")
    print(f"Result: {random_number * s}")


if __name__ == "__main__":
    main()
