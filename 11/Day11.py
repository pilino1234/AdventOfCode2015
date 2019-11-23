
def increment_password(pwd: str) -> str:
    letters = [l for l in pwd]

    increase_next, new_letter = divmod(ord(letters[-1]) + 1 - 97, 26)

    if any(new_letter + 97 == ord(banned_letter) for banned_letter in 'iol'):
        new_letter += 1
    new_letter = chr(new_letter + 97)

    letters[-1] = new_letter
    if increase_next:
        if len(pwd) > 1:
            left = increment_password(pwd[:-1])
            return left + new_letter
    return "".join(letters)


def valid(pwd: str) -> bool:
    if not pwd.islower() or len(pwd) != 8:
        return False
    if any(letter in pwd for letter in 'iol'):
        return False

    contains_increasing_straight = False
    pairs = 0
    for idx, letter in enumerate(pwd):
        if idx == 0 or idx == 1:
            continue

        if letter == pwd[idx-1] and (letter != pwd[idx-2] if idx > 1 else True):
            pairs += 1

        if idx > 1:  # Check for increasing straight
            if ord(letter) == ord(pwd[idx-1]) + 1 == ord(pwd[idx-2]) + 2:
                contains_increasing_straight = True

    if not contains_increasing_straight or not pairs == 2:
        return False

    return True


if __name__ == '__main__':
    starting_password = "cqjxjnds"

    password = increment_password(starting_password)
    for _ in range(2):
        while not valid(password):
            # print(password, valid(password))
            password = increment_password(password)
        print(password, valid(password))
        password = increment_password(password)

