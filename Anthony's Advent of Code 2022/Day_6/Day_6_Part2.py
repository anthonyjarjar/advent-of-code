INPUT = "Anthony's Advent of Code 2022/Day_6/input.txt"


def extract_input(filename):
    file = open(filename, 'r')
    return list(file.read().splitlines())


def check(entry):
    for k in range(len(entry)):
        for j in range(k + 1, len(entry)):
            if entry[k] == entry[j]:
                return False

    return True


def function(list):
    for i in range(4092):
        entry = list[0][i:i + 14]

        if check(entry):
            return print(i + 14)
        else:
            pass

        i += 1


def main():
    lines = extract_input(INPUT)
    function(lines)


if __name__ == '__main__':
    main()
