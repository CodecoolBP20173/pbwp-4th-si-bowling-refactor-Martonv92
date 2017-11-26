def get_value(char):
    try:
        return int(char)
    except ValueError:
        if char.upper() == 'X' or char == '/':
            return 10
        elif char == '-':
            return 0
        raise ValueError()


def score(game):
    result, frame = 0, 1
    frame_limit = 10
    in_first_half = True

    for i in range(len(game)):
        try:
            is_spare = (game[i + 1] == "/")
        except IndexError:
            is_spare = False

        if not is_spare:
            result += get_value(game[i])

            if game[i].upper() == "X":
                result += get_value(game[i + 1]) + get_value(game[i + 2])
                in_first_half = False

            if game[i] == "/":
                in_first_half = False
        else:
            result += get_value(game[i + 2])

        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half

        if frame > frame_limit:
            break

    return result