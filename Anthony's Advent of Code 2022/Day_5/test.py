

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

    for i in manifestDict.keys():
        manifestDict[i] = manifestDict[i][::-1]

    return manifestDict


def getMoves(moves, crates):
    manifestDict = createDict(crates)
    removeArr = []
    addArr = []
    amountArr = []

    for move in moves:
        moveArr = move.replace("move ", '').replace(
            " from ", ' ').replace(" to ", ' ').split()

        removeArr.append(moveArr[1])
        addArr.append(moveArr[2])
        amountArr.append(moveArr[0])

    for i, amount in enumerate(amountArr[:1]):
        manifestDict[addArr[i]].append(
            manifestDict[removeArr[i][:int(amount)]])
        for j in range(int(amount)):
            manifestDict[removeArr[i]].pop()
        print(f"Move {i} completed")

    for i in manifestDict:
        print(manifestDict[str(i)])

    for i in range(int(moveArr[0])):
        manifestDict[add] += manifestDict[[remove][0]]
        manifestDict[remove].pop(0)

        gc.collect()

    gc.collect()

    print(manifestDict)
    """


def main():
    crates = extract_input(inputCrates)
    moves = extract_input(inputMoves)

    getMoves(moves, crates)


if __name__ == '__main__':
    main()
