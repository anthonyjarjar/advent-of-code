INPUT = 'Day_1/input.txt'


def extract_input(filename):
    file = open(filename, 'r')
    return list(file.read().splitlines())


def function(list):

    currentCalorieCount = 0
    highestCalorieCount = 0

    for entries in list:

        if entries == '':
            if currentCalorieCount >= highestCalorieCount:
                highestCalorieCount = currentCalorieCount
                currentCalorieCount = 0
            else:
                currentCalorieCount = 0
        else:
            currentCalorieCount += int(entries)

    return print(highestCalorieCount)


def main():
    lines = extract_input(INPUT)
    function(lines)


if __name__ == '__main__':
    main()
