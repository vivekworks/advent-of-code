spelled_out_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def read_file():
    f = open("input.txt", "r")
    calib_sum = 0
    for line in f:
        first = -1
        last = -1
        p1 = 0
        while p1 < len(line):
            if line[p1].isnumeric():
                last = int(line[p1])
                if first == -1:
                    first = int(line[p1])
            else:
                i = 3
                while i <= 5:
                    if p1 + i >= len(line):
                        break
                    txt = line[p1:p1 + i]
                    val = spelled_out_digits.get(txt)
                    if val is None:
                        i = i + 1
                        continue
                    else:
                        if first == -1:
                            first = val
                            last = val
                        else:
                            last = val
                    break
            p1 = p1 + 1
        calib_sum += (first * 10) + last
    return calib_sum


if __name__ == "__main__":
    print(read_file())
