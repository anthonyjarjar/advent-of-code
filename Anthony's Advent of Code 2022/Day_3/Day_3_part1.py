import numpy as np

INPUT = 'Day_3/input.txt'

value = ["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def extract_input(filename):
    file = open(filename, 'r')
    return list(file.read().splitlines())


def function(list):
    index = []
    total = 0

    for entries in list:
        firstHalf = []
        secondHalf = []

        for x in range(int(len(entries) / 2)):
            firstHalf.append(entries[x])

        for x in range(int(len(entries) / 2)):
            secondHalf.append(entries[(x) + (int(len(entries) / 2))])

        np_firstHalf = np.array(firstHalf)
        np_secondHalf = np.array(secondHalf)

        repeat = np.intersect1d(np_firstHalf, np_secondHalf)

        index.append(repeat[0])

    for i in index:
        x = 0
        for j in value:
            if i == j:
                total += x
            else:
                x += 1
                pass
    print(total)


def main():
    lines = extract_input(INPUT)
    function(lines)


if __name__ == '__main__':
    main()
