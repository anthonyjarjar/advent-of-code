import gc

inputMoves = "Anthony's Advent of Code 2022/Day_5/InputMoves.txt"
inputCrates = "Anthony's Advent of Code 2022/Day_5/InputCrates.txt"


def extract_input(filename):
    file = open(filename, 'r')
    return list(file.read().splitlines())


def createDict(crates):
    x = 1

    manifestDict = {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],
    }

    for crate in crates:
        manifestDict[str(x)] = [i for i in crate]
        x = x + 1

    return manifestDict


def getMoves(moves, crates):
    manifestDict = createDict(crates)

    for i in manifestDict:
        print(i, manifestDict[str(i)])

    for move in moves:
        temp = []
        moveArr = move.replace("move ", '').replace(
            " from ", ' ').replace(" to ", ' ').split()

        remove = moveArr[1]
        add = moveArr[2]

        for i in range(int(moveArr[0])):
            temp.append(manifestDict[remove].pop())

        manifestDict[add] += temp[::-1]

    for i in manifestDict:
        print(manifestDict[str(i)][-1], end='')

    print("\n")

    for i in manifestDict:
        print(i, manifestDict[str(i)])


def main():
    crates = extract_input(inputCrates)
    moves = extract_input(inputMoves)

    getMoves(moves, crates)


if __name__ == '__main__':
    main()
