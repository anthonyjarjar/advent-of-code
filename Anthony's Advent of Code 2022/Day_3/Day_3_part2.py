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
    x = -2
    y = -1
    z = 0

    for i in range(100):

        backpack1 = list[x + 3]
        backpack2 = list[y + 3]
        backpack3 = list[z + 3]

        backpack1 = set(backpack1)
        backpack2 = set(backpack2)

        x += 3
        y += 3
        z += 3

        set1 = ''.join(sorted(backpack1.intersection(backpack2)))

        set1 = set(set1)

        index.append(''.join(sorted(set1.intersection(backpack3))))

    for i in index:
        n = 0
        for j in value:
            if i == j:
                total += n
            else:
                n += 1
                pass
    print(total)

def main():
    lines = extract_input(INPUT)
    function(lines)


if __name__ == '__main__':
    main()
