def sum_of_ids():
    input_data = get_input_data()
    red, green, blue = 12, 13, 14
    score = 0
    for line in input_data:
        game_index = line.index(':')
        sets = line[game_index + 1:].strip()
        game_score_index = line[:game_index].index(' ')
        game_score = int(line[game_score_index:game_index].strip())
        include_score = True
        for s in sets.split(";"):
            if len(s.strip()) <= 0:
                break
            for cube in s.split(","):
                cube = cube.strip()
                index = cube.index(' ')
                num = int(cube[:index].strip())
                cube_type = cube[index:].strip().lower()
                if ((cube_type == "red" and num > red) or (cube_type == "green" and num > green) or
                        (cube_type == "blue" and num > blue)):
                    include_score = False
        if include_score:
            score += game_score
    return score


def power_of_sets():
    input_txt = get_input_data()
    power = 0
    for line in input_txt:
        game_index = line.index(':')
        sets = line[game_index + 1:].strip()
        max_red, max_green, max_blue = 1, 1, 1
        for s in sets.split(";"):
            if len(s.strip()) <= 0:
                break
            for cube in s.split(","):
                cube = cube.strip()
                index = cube.index(' ')
                num = int(cube[:index].strip())
                cube_type = cube[index:].strip().lower()
                if cube_type == 'red' and num > max_red:
                    max_red = num
                if cube_type == 'green' and num > max_green:
                    max_green = num
                if cube_type == 'blue' and num > max_blue:
                    max_blue = num
        power += (max_blue * max_green * max_red)
    return power


def get_input_data():
    return open("input.txt", "r")


if __name__ == "__main__":
    print(power_of_sets())
