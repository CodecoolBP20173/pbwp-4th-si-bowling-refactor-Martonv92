# the function that is used in another function should be defined first.
def get_value(char):
    # if char can be converted to int, then it's a number.
    try:
        return int(char)
    except ValueError:
        # both "/" and "X" mean 10
        if char.upper() == 'X' or char == '/':
            return 10
        elif char == '-':
            return 0
        # if none of the above can run, ValueError is raised
        raise ValueError()


def score(game):
    result, frame = 0, 1
    frame_limit = 10
    in_first_half = True

    for i in range(len(game)):
        # is_spare helps us stay in the index range
        try:
            is_spare = (game[i + 1] == "/")
        except IndexError:
            is_spare = False

        if not is_spare:
            result += get_value(game[i])

            # the .upper method enables us to evaluate both "x" and "X"
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

        # this is where the game ends.
        if frame > frame_limit:
            break

    return result
