INPUT = 'Day_2/input.txt'

possible_attempts = [
    ["A X", "4"],
    ["A Y", "8"],
    ["A Z", "3"],
    ["B X", "1"],
    ["B Y", "5"],
    ["B Z", "9"],
    ["C X", "7"],
    ["C Y", "2"],
    ["C Z", "6"]
]


def extract_input(filename):
    file = open(filename, 'r')
    return list(file.read().splitlines())


def function(list):
    total = 0

    for entries in list:
        for x in range(9):
            if entries == possible_attempts[x][0]:
                total += int(possible_attempts[x][1])
            else:
                pass

    return(print(total))


def main():
    lines = extract_input(INPUT)
    function(lines)


if __name__ == '__main__':
    main()
