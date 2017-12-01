
def strlen_total_chars(strings):
    return sum(len(string) for string in strings)

def strlen(strings):
    pass

if __name__ == "__main__":
    print(strlen_total_chars("asdf"))
    print(strlen_total_chars('"asdf"'))
    print(strlen_total_chars('"\"asdf\""'))
    
    with open("Day8-input.txt") as file:
        lines = file.read().splitlines()

    print(strlen_total_chars(lines))
    print(strlen([lines[1:-1] for line in lines]))
