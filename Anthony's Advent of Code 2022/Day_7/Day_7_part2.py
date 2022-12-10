INPUT = "Anthony's Advent of Code 2022/Day_7/input.txt"


def extract_input(filename):
    file = open(filename, 'r')
    return list(file.read().splitlines())


def function(list):

    currDir = []
    dirSize = []

    def compile():
        dirSize.append(currDir.pop(-1))

        if currDir:
            currDir[-1] += dirSize[-1]

        for line in list:
            match  line.strip().split():
                case "$", "cd", "..": compile()
                case "$", "cd", _: currDir.append(0)
                case "$", _: pass
                case "dir", _: pass
                case size, _: currDir[-1] += int(size)

        while currDir:
            compile()

        print(min(s for s in dirSize if s >= (max(dirSize) - 40000000)))


def main():
    lines = extract_input(INPUT)
    function(lines)


if __name__ == '__main__':
    main()
