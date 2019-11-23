
def look_and_say(sequence: str) -> str:
    numbers = [c for c in sequence]

    output = ""

    current_counter = 0
    current_number = None
    for num in numbers:
        if current_number is None:
            current_number = num
        if num == current_number:
            current_counter += 1
        else:
            output += str(current_counter) + str(current_number)
            current_number = num
            current_counter = 1

    # Add the last number before the loop ended
    output += str(current_counter) + str(current_number)

    return output


if __name__ == '__main__':
    seed = "3113322113"

    # Part 1
    result = look_and_say(seed)
    for _ in range(40 - 1):
        result = look_and_say(result)
    print(len(result))

    # Part 2
    result = look_and_say(seed)
    for _ in range(50-1):
        result = look_and_say(result)
    print(len(result))
