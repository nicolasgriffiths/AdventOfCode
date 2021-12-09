from dataclasses import dataclass
from typing import List

INPUT_FILE_PATH = "2021/8/input.txt"


@dataclass
class Display:
    codes: List[str]
    outputs: List[str]


def solve_display(display: Display):
    code_to_num, num_to_code = {}, {}
    lengths = [len(code) for code in display.codes]
    # 1 is the only number of length 2
    code_to_num[display.codes[lengths.index(2)]] = 1
    num_to_code[1] = display.codes[lengths.index(2)]
    # 7 is the only number of length 3
    code_to_num[display.codes[lengths.index(3)]] = 7
    num_to_code[7] = display.codes[lengths.index(3)]
    # 4 is the only number of length 4
    code_to_num[display.codes[lengths.index(4)]] = 4
    num_to_code[4] = display.codes[lengths.index(4)]
    # 8 is the only number of length 7
    code_to_num[display.codes[lengths.index(7)]] = 8
    num_to_code[8] = display.codes[lengths.index(7)]
    # Of all elements of length 6 (0, 6 and 9) find the one that does not share all elements of 1: It must be 6
    indices_of_len_6 = [idx for idx in range(len(lengths)) if lengths[idx] == 6]
    codes_of_len_6 = [display.codes[idx] for idx in indices_of_len_6]
    for code in codes_of_len_6:
        for char in num_to_code[1]:
            if not char in code:
                code_to_num[code] = 6
                num_to_code[6] = code
    # Of all elements of length 5 (2, 3 and 5) find the one that is a subset of 6: It must be 5
    indices_of_len_5 = [idx for idx in range(len(lengths)) if lengths[idx] == 5]
    codes_of_len_5 = [display.codes[idx] for idx in indices_of_len_5]
    for code in codes_of_len_5:
        if all(char in num_to_code[6] for char in code):
            code_to_num[code] = 5
            num_to_code[5] = code
    # Of all elements left of length 6 (0 and 9) find the one that is a superset of 4: It must be 9
    codes_of_len_6.remove(num_to_code[6])
    for code in codes_of_len_6:
        if all(char in code for char in num_to_code[4]):
            code_to_num[code] = 9
            num_to_code[9] = code
    codes_of_len_6.remove(num_to_code[9])
    # The only element left of length 6 must be 0
    assert len(codes_of_len_6) == 1
    code_to_num[codes_of_len_6[0]] = 0
    num_to_code[0] = codes_of_len_6[0]
    # Of all elements left of length 5 (2 and 3) find the one that is a a subset of 9: It must be 3
    codes_of_len_5.remove(num_to_code[5])
    for code in codes_of_len_5:
        if all(char in num_to_code[9] for char in code):
            code_to_num[code] = 3
            num_to_code[3] = code
    codes_of_len_5.remove(num_to_code[3])
    # The only element left of length 5 must be 2
    assert len(codes_of_len_5) == 1
    code_to_num[codes_of_len_5[0]] = 2
    num_to_code[2] = codes_of_len_5[0]

    return [code_to_num[output] for output in display.outputs]


def main():
    with open(INPUT_FILE_PATH, "r") as f:
        displays = []
        for line in f.readlines():
            codes, outputs = line.strip().split("|")
            all_codes, all_outputs = [], []
            for code in codes.strip().split(" "):
                all_codes.append("".join(sorted(code)))
            for output in outputs.strip().split(" "):
                all_outputs.append("".join(sorted(output)))
            displays.append(Display(codes=all_codes, outputs=all_outputs))

    outputs = [solve_display(d) for d in displays]
    result = 0
    for output in outputs:
        num = 0
        for i, digit in enumerate(reversed(output)):
            num += digit * (10 ** i)
        result += num

    print(result)


if __name__ == "__main__":
    main()
