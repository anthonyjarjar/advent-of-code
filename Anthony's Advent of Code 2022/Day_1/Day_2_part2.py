INPUT = 'Day_1/input.txt'


def extract_input(filename):
    file = open(filename, 'r')
    return list(file.read().splitlines())


def function(list):
    calorieTotal = 0
    index = []

    for entries in list:
        if entries == '':
            index.append(calorieTotal)
            calorieTotal = 0
        else:
            calorieTotal += int(entries)

    index.sort(reverse=True)

    return print(index[0] + index[1] + index[2])


def main():
    lines = extract_input(INPUT)
    function(lines)


if __name__ == '__main__':
    main()
